""""
Master script that determine and iterate over the different boxes arrangement.
Call the different Ros Services. Initialize and set parameters to Gazebo.
"""

import rospy
from box_generator.srv import SpawnBox, SpawnBoxRequest, SetParam, SetParamRequest, DeleteBox, DeleteBoxRequest, WaypointSender, WaypointSenderRequest
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

class BoxIT_Manager:
    def __init__(self):
        # Setup
        rospy.init_node('BoxIt_master')

        rospy.loginfo("Master node listening.")

        # Arguments
        self.mqtt_params = None
        self.boxes_id = None
        self.fail_flag = False

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
        self.ref_time = None

        self.obj = MikelObj()

    @property
    def is_ready(self):
       # TODO: self.optimizator.is_ready()
       return self.mqtt_params != None
    
    def run(self):
        # Run first empty trial- max score:
        self.first_tune()

        
        # Start the main loop in a separate thread
        self.main_loop_thread = threading.Thread(target=self.main_loop)
        self.main_loop_thread.daemon = True
        self.main_loop_thread.start()

        rospy.spin()

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
            # TODO: Generate layout()
            # self.optizimer.get_layout()
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
    
    def get_gazebo_time(self):
        return self.gazebo_time
    
    def spawn_boxes(self, layout):
        rospy.wait_for_service('spawn_box')

        try:
            spawn_box = rospy.ServiceProxy('spawn_box', SpawnBox)

            # Generate boxes name:
            self.boxes_id = ["Box_"+str(i) for i in range(len(layout.position))]

            # Spawn Boxes
            req = SpawnBoxRequest(
            boxes_id = self.boxes_id,
            mass = args['mass'],
            length = args['lenght'],
            width = args['width'],
            height = args['heigth']
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


        # self.arm_client.wait_for_result()

        # # Return True if the goal was reached
        # if self.arm_client.get_state() == GoalStatus.SUCCEEDED:
        #     rospy.loginfo("Goal succeeded!")
        #     return True
        # else:
        #     rospy.logwarn("Goal failed or was aborted.")
        #     return False
    
    ############### BOX IT! UTILS #############################

    def navigation_routine(self):
        
        # Threading events
        stop = threading.Event()
        done = threading.Event()
        
        # Init time:
        start_time = self.get_gazebo_time()
        end_time = None
        sucess = True

        # Start the main loop in a separate thread
        self.nav_thread = threading.Thread(target=self.send_waypoints,args=(stop,done))
        self.nav_thread.daemon = True
        self.nav_thread.start()

        while done.is_set() == False:

            if self.fail_flag:
                stop.set()
                end_time = self.get_gazebo_time()
                sucess = False
                break 
            
            time.sleep(0.1)
        
        # If sucess assign last ros time
        if sucess:
            end_time = self.get_gazebo_time()
            rospy.loginfo("All goals processed.")
        else:
            rospy.loginfo("Failed trial.")
        
        trialtime = end_time - start_time

        return sucess, trialtime
    
    
    def send_waypoints(self,args):
        """
        This function sends a sequence of navigation goals to a robot.
        Output reward of trial in form of simulation time.
        """

        rospy.wait_for_service('router')

        try:
            send_waypoint = rospy.ServiceProxy('router', WaypointSender)

           
            for goal_data in self.goal_list:
                if args.stop.is_set() == False:
                    position = goal_data['position']
                    orientation = goal_data['orientation']

                    # Spawn Boxes
                    req = WaypointSenderRequest(
                    position_x = goal_data['position']['x'],
                    position_y = goal_data['position']['y'],
                    position_z = goal_data['position']['z'],
                    orientation_x = goal_data['orientation']['x'],
                    orientation_y = goal_data['orientation']['y'],
                    orientation_z = goal_data['orientation']['z'],
                    orientation_w = goal_data['orientation']['w']
                    )

                    send_waypoint(req)    # Locking process              
            
        except rospy.ServiceException as e:
            print("Error - couldn't get spawn_box service: %s" % e)    
        
  
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
        while rospy.is_shutdown:
            # if not self.is_ready:
            #     self.mqtt_params = dict()
            #     self.mqtt_params['n_boxes'] = 6
            #     self.mqtt_params['mass'] = 0.5
            #     self.mqtt_params['lenght'] = 0.2
            #     self.mqtt_params['width'] = 0.2
            #     self.mqtt_params['height'] = 0.2
            
            if self.is_ready:
 
                user_params = self.get_user_param()


                # TODO: 
                layout = self.optimizator.get_next_layout()
                
                # TODO: Compute orientations
                # TODO: Compute posible poses
        

                # TODO: Sabina algorithm:
                box_param, mir_params = self.sabina_loop()

                # Set robot params
                rospy.loginfo(f"Set robot parameters")
                self.set_param(mir_params)
            
                rospy.loginfo(f"Spawning boxes...")
                self.spawn_boxes(layout)
                time.sleep(0.2)
               
                # Navigation - simulation trial
                rospy.loginfo(f"Wait while navegation happening...")
                sucess, trial_time = self.navigation_routine()

                rospy.loginfo(f"Deleting boxes and restart the simulation.")
                self.reset_gazebo()
                self.delete_model()
                
                self.optimizator.set_score(current_layout = layout, score = (sucess, trial_time))
                layout.set_score 
            time.sleep(1)

    
    def first_run(self):
                
        rospy.loginfo("Init refernce trial  ")

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
        _, trrial_time = self.navigation_routine()
        

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

    
