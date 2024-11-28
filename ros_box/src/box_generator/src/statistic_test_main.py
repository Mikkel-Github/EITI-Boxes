""""
Master script that determine and iterate over the different boxes arrangement.
Call the different Ros Services. Initialize and set parameters to Gazebo.
"""

import rospy
from box_generator.srv import SpawnBox, SpawnBoxRequest, SetParam, SetParamRequest, DeleteBox, DeleteBoxRequest, MqttListener, MqttListenerRequest
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
import actionlib
from std_msgs.msg import Bool
from std_srvs.srv import Empty
from rosgraph_msgs.msg import Clock
from geometry_msgs.msg import Pose, Quaternion
from gazebo_msgs.msg import LinkStates 
import tf.transformations as tft
import paho.mqtt.client as mqtt
import json
import threading
import time
import numpy as np
import tf.transformations as tr
import math


# Global parameters: Defined for MIR100
MAX_HEIGHT = 2 # meters
MAX_WIDTH = 0.60
MAX_LENGHT = 0.80
MAX_N_CONFIGURATIONS = 100

class BoxIT_Manager:
    def __init__(self):
        # Setup
        rospy.init_node('BoxIt_master')

        rospy.loginfo("Master node listening.")

        # Arguments
        self.mqtt_params = None
        self.boxes_id = None
        self.fail_flag = False
        self.mir_pose = None
        self.ref_time = None

        # User Taylored environment params:
        # TODO: Consider functionalities to select type of robot, map and path to follow
        self.robot_id = 'Mir'
        self.map = None
        self.path = None

        # Init MQTT client
        try:
            self.mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            self.mqtt_client.on_connect = self.on_connect
            self.mqtt_client.on_message = self.on_message
            self.mqtt_client.connect("ec2-16-16-27-107.eu-north-1.compute.amazonaws.com", 1883, 60)

            # Start the MQTT loop in a separate thread
            self.mqtt_thread = threading.Thread(target=self.run_mqtt)
            self.mqtt_thread.daemon = True  # Set daemon so it shuts down on exit
            self.mqtt_thread.start()

            rospy.loginfo("Ready to receive MQTT request")

        except:
            pass
            
        # Suscriptions to topics:
        rospy.Subscriber('/reset_sim', Bool, self.check_fails)
        rospy.Subscriber('/clock', Clock, self.callback_time)
        rospy.Subscriber('/gazebo/link_states', LinkStates, self.callback_mir_pose)

        # Movebase client - send target points to AMR:
        self.arm_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.arm_client.wait_for_server()

        # Waypoint list - equal for every trial
        self.goal_list = [
            {
                'position': {'x': 16.67, 'y': 2.76, 'z': 0.0},
                'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': -0.7}  # BASE
            },
            {
                'position': {'x': 7.2, 'y': 2.79, 'z': 0.0},
                'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.99}  # STOP1
            },
            # ... other goals ...
        ]
        

    @property
    def is_ready(self):
       return self.mqtt_params != None
    
    def run(self):
        rospy.spin()
        # Run first empty trial- max score:
        print("Something")
        self.first_run()

        # Start the main loop in a separate thread
        self.main_loop_thread = threading.Thread(target=self.main_loop)
        self.main_loop_thread.daemon = True
        self.main_loop_thread.start()

        

    def check_fails(self, msg):
        self.fail_flag = msg.data
    
    ################## MQTT Listener ###########################
    def run_mqtt(self):
        # Start MQTT client loop, listening for messages
        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        self.mqtt_client.loop_forever()

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(_, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("box_spawner/spawn")
        client.subscribe("box_spawner/delete") # don't know if we need this
        client.subscribe("box_spawner/reset")
    
    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(str(msg.payload))
        payload = ""
        if(str(msg.payload) != "b''"): # Payload is NOT empty
            payload = json.loads(msg.payload)

        print(msg.topic + " " + str(payload))

        if(str(msg.topic) == "box_spawner/spawn"):
            self.mqtt_params = payload
        else:
            print('Not matching topic!')
    
    def get_user_param(self):
        # Convert from string to actual type
        args = dict()
        args['n_boxes'] = int(self.mqtt_params['n_boxes'])
        args['mass'] = float(self.mqtt_params['mass'])
        args['lenght'] = float(self.mqtt_params['lenght'])/100
        args['width'] = float(self.mqtt_params['width'])/100
        args['heigth'] = float(self.mqtt_params['height'])/100

        return args

    ################## MIR Robot UTILS #########################
    def set_param(self, args):
        rospy.wait_for_service('set_param')

        try:
            set_param_srv = rospy.ServiceProxy('set_param', SetParam)

            # Generate boxes name:
            self.boxes_id = ["Box_"+str(i) for i in range(args['n_boxes'])]

            # Set boxes request:
            req = SetParamRequest(
            max_speed_xy = args['max_speed_xy'],
            max_vel_x = args['max_vel_x'],
            acc_lim_x = args['acc_lim_x'],
            decel_lim_x = args['decel_lim_x'],
            max_vel_theta = args['max_vel_theta']
            )

            set_param_srv(req)
            
        except rospy.ServiceException as e:
            print("Error - couldn't get spawn_box service: %s" % e)

    ################## GAZEBO UTILS ############################
    def callback_time(self, msg):
        sec = msg.clock.secs
        nano = msg.clock.nsecs
        self.gazebo_time = sec + nano/1e9
    
    def callback_mir_pose(self, msg):
        for name, pose in zip(msg.name, msg.pose):
            if name == "mir::base_footprint":
                self.mir_pose = pose
    
    def get_gazebo_time(self):
        return self.gazebo_time
    
    def spawn_boxes(self, args):
        rospy.wait_for_service('spawn_box')

        try:
            spawn_box = rospy.ServiceProxy('spawn_box', SpawnBox)

            # Generate boxes name:
            self.boxes_id = ["Box_"+str(i) for i in range(args['n_boxes'])]

            # Spawn Boxes
            req = SpawnBoxRequest(
            boxes_id = self.boxes_id,
            mass = args['mass'],
            length = args['lenght'],
            width = args['width'],
            height = args['heigth'],
            poses = args['poses']
            )

            spawn_box(req)
            
        except rospy.ServiceException as e:
            print("Error - couldn't get spawn_box service: %s" % e)

    
    def reset_gazebo(self):
        rospy.wait_for_service('/gazebo/reset_simulation')
        try:
            reset_sim = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
            reset_sim()  
            print("World reseted!.")
        except rospy.ServiceException as e:
            print("Error reseting world: %s" % e)

    def delete_model(self):
        rospy.wait_for_service('/gazebo/delete_model')
        
        try:
            # Create a client for the delete service
            delete_box = rospy.ServiceProxy('delete_box', DeleteBox)
            req = DeleteBoxRequest(self.boxes_id)
            delete_box(req)
          
        except rospy.ServiceException as e:
            rospy.logerr(f"Error calling Gazebo delete model service: {e}")

    def send_goal(self, goal_position, goal_orientation):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        goal.target_pose.pose.position.x = goal_position['x']
        goal.target_pose.pose.position.y = goal_position['y']
        goal.target_pose.pose.position.z = goal_position['z']

        goal.target_pose.pose.orientation.x = goal_orientation['x']
        goal.target_pose.pose.orientation.y = goal_orientation['y']
        goal.target_pose.pose.orientation.z = goal_orientation['z']
        goal.target_pose.pose.orientation.w = goal_orientation['w']

        rospy.loginfo("Sending goal: position=({}, {}, {}), orientation=({}, {}, {}, {})".format(
            goal_position['x'], goal_position['y'], goal_position['z'],
            goal_orientation['x'], goal_orientation['y'], goal_orientation['z'], goal_orientation['w']
        ))

        self.arm_client.send_goal(goal)
    
    ############### BOX IT! UTILS #############################
    def navigation_routine(self):
        """
        This function sends a sequence of navigation goals to a robot.
        Output reward of trial in form of simulation time.
        """

        start_time = self.get_gazebo_time()
        end_time = None
        sucess = True
        for goal_data in self.goal_list:
            position = goal_data['position']
            orientation = goal_data['orientation']

            self.send_goal(position, orientation)

            while self.arm_client.get_state() != GoalStatus.SUCCEEDED:

                if self.fail_flag:
                    end_time = self.get_gazebo_time()
                    sucess = False
                    break 
                
                time.sleep(0.1)
            
            if end_time != None: break
        
        # If sucess assign last ros time
        if sucess:
            end_time = self.get_gazebo_time()
            rospy.loginfo("All goals processed.")
        else:
            rospy.loginfo("Failed trial.")
        
        trial_time = end_time - start_time

        score = self.compute_score(trial_time)

        return sucess, score

    def boxes_placement(self, n_boxes, width, length, height):
        # NOTE: This script create a matrix of ros Pose where to place the boxes
        assert self.mir_pose is not None


        # Dimension of arrangement matrix:
        max_num_box_width = int(MAX_WIDTH / width)
        max_num_box_length = int(MAX_LENGHT / length)
        max_num_box_height = int(MAX_HEIGHT / height)

        max_capacity = max_num_box_height*max_num_box_length*max_num_box_width # Maximun number of boxes that can be carried
        max_boxes_per_layer = max_num_box_width*max_num_box_length

        print("Max capacity: ", max_capacity)
        
        if n_boxes > max_capacity:
        # TODO: If n boxes exceed the max capacity do something
            pass

        # Compute Center of Gravity stack of boxes:
        cog_width = (width*max_num_box_width)/2
        cog_length = (length*max_num_box_length)/2
        translation_cog_origin = np.array([cog_length, cog_width, 0])
        
        # Translation and rotation matrix from MIR base pose    
        translation_origin_mir = [self.mir_pose.position.x, self.mir_pose.position.y, self.mir_pose.position.z + 0.2]
        quaternion = [self.mir_pose.orientation.x, self.mir_pose.orientation.y, self.mir_pose.orientation.z, self.mir_pose.orientation.w]
        rotation_matrix = tr.quaternion_matrix(quaternion)[0:3,0:3]

        # Define position matrix:
        pose_list = []
        cont = 0
        break_all = False
        # Layer dimension:
        for k in range(max_num_box_height):
            boxes_left = n_boxes - cont
            print(boxes_left)
            if boxes_left < max_boxes_per_layer:
                num_width_this_layer = max_num_box_width
                num_length_this_layer = math.ceil(boxes_left/num_width_this_layer)
            
            else:
                num_width_this_layer = max_num_box_width
                num_length_this_layer = max_num_box_length

            # Layer CoG:
            cog_width = (width*num_width_this_layer)/2
            cog_length = (length*num_length_this_layer)/2
            translation_cog_origin = np.array([cog_length, cog_width, 0])
            
            for j in range(num_width_this_layer):
                for i in range(num_length_this_layer):
                    if cont < n_boxes and cont < max_capacity:
                        cont = cont + 1

                        # Compute single box CoG:
                        x = i*length + length/2 
                        y = j*width + width/2 
                        z = k*height + height/2 
                        box_pose = np.array([x,y,z])

                        # Translation to base frame:
                        box_pose_origin = box_pose - translation_cog_origin

                        # Rotation & translate to MIR orientation:
                        box_pose_mir = np.dot(rotation_matrix, box_pose_origin)
                        box_pose_mir = box_pose_mir + translation_origin_mir

                        pose = Pose()
                        pose.position.x = box_pose_mir[0] 
                        pose.position.y = box_pose_mir[1] 
                        pose.position.z = box_pose_mir[2] 
                        pose.orientation = self.mir_pose.orientation

                        pose_list.append(pose)
                    else:
                        break_all = True
                        break
                if break_all:
                    break
            if break_all:
                break
                
        return pose_list
    
    #################### MAIN LOOP #####################

    def compute_score(self, succes, t):
        if self.ref_time is None:
            self.ref_time = t
            return 1
        else:
            if succes:
                score = self.ref_time/t # [0,1]
            else:
                score = 0
            return score
        
    def main_loop(self):

        # Define values for the text:
        n_boxes = 10
        mass = 6
        length = 0.2
        width = 0.2
        height = 0.2
        

        # Possible combinations:
        orientation_list = [
                            [length, width, height],
                            [width, length, height],
                            [length, height,width],
                            [height, length, width],
                            [width, height, length],
                            [height, width,length],
        ]

        

        mir_params = [  # max_speed_xy, max_vel_x, acc_lim_x, decel_lim_x, max_vel_theta
                        [0.8, 0.5, 1.5, 1.5, 1]
        ]

        
        while rospy.is_shutdown:
            
            for orientation, mir_config in zip(orientation_list, mir_params):
                rospy.loginfo("Iter started")
                # Mir params:
                mir_params = {
                    'max_speed_xy': mir_config[0],
                    'max_vel_x': mir_config[1],
                    'acc_lim_x': mir_config[2],
                    'decel_lim_x': mir_config[3],
                    'max_vel_theta': mir_config[4]
                }    

                # Set robot params
                rospy.loginfo(f"Set robot parameters")
                self.set_param(mir_params)

                # Get orientation
                width = orientation[0]
                height = orientation[1]
                lenght = orientation[2] 

                # Compute poses for boxes:
                poses = self.boxes_placement(n_boxes, width, lenght, height)

                box_param = dict()
                box_param['mass'] = mass
                box_param['length'] = lenght
                box_param['width'] = width
                box_param['height'] = height
                box_param['poses'] = poses
                
                rospy.loginfo(f"Spawning boxes...")
                self.spawn_boxes(box_param)
                time.sleep(0.2)
               
                # Navigation - simulation trial
                rospy.loginfo(f"Wait while navegation happening...")
                sucess, trial_time = self.navigation_routine()

                rospy.loginfo(f"Deleting boxes and restart the simulation.")
                self.reset_gazebo()
                self.delete_model()
                

                time.sleep(1)

    
    def first_run(self):
                
        rospy.loginfo("Init reference trial  ")

        # Set MAX robot params  
        mir_params = {
            'max_speed_xy': 0.8,
            'max_vel_x': 0.8,
            'acc_lim_x': 1.5,
            'decel_lim_x': 1.5,
            'max_vel_theta': 1.0
        }    

        # Set robot params
        rospy.loginfo(f"Set max robot parameters")
        self.set_param(mir_params)
        _, score = self.navigation_routine()
        

        rospy.loginfo(f"Reference score saved!")
        self.reset_gazebo()
        

        time.sleep(1)

        

if __name__ == '__main__':
    try:
        node = BoxIT_Manager()
        node.run()
    except rospy.ROSInterruptException:
        pass

    #   # Delete boxes:
    #   print('----> Hit enter to delete models.')
    #   a = input()

    #   req = DeleteBoxRequest(
    #      boxes_id = boxes_id
    #   )
    #   delete_box(req)
    
    
    #   print('----> Hit enter to reset the world.')
    #   a = input()
    #   reset_gazebo()

    
