""""
This service client script is used to test the SpawnBox service
"""

import rospy
from box_generator.srv import SpawnBox, SpawnBoxRequest, DeleteBox, WaypointSender, WaypointSenderRequest, SetParam, SetParamRequest
from gazebo_msgs.srv import SpawnModel, DeleteModel
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_srvs.srv import Empty
from geometry_msgs.msg import Pose, Quaternion
from gazebo_msgs.msg import LinkStates 
import tf.transformations as tft
import random
import math
import numpy as np
import tf.transformations as tr
from actionlib_msgs.msg import GoalStatus
import actionlib
import time
import threading

# Global parameters: Defined for MIR100
MAX_HEIGHT = 2 # meters
MAX_WIDTH = 0.60
MAX_LENGHT = 0.80
MAX_N_CONFIGURATIONS = 100

################## GAZEBO UTILS ############################
global mir__pose

def callback_mir_pose(msg):
  global mir_pose
  for name, pose in zip(msg.name, msg.pose):
      if name == "mir::base_footprint":
          mir_pose = pose

def boxes_placement(n_boxes, width, length, height):
        global mir_pose
        # NOTE: This script create a matrix of ros Pose where to place the boxes
        assert mir_pose is not None


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
        translation_origin_mir = [mir_pose.position.x, mir_pose.position.y, mir_pose.position.z + 0.2]
        quaternion = [mir_pose.orientation.x, mir_pose.orientation.y, mir_pose.orientation.z, mir_pose.orientation.w]
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
                        pose.orientation = mir_pose.orientation

                        pose_list.append(pose)
                    else:
                        break_all = True
                        break
                if break_all:
                    break
            if break_all:
                break
                
        return pose_list
  
def navigation_routine():
    
    # Threading events
    stop = threading.Event()
    done = threading.Event()
    stop.clear()
    done.clear()
    
    # Init time:
    end_time = None
    sucess = True

    # Start the main loop in a separate thread
    nav_thread = threading.Thread(target=send_waypoints, args=(stop,done))
    nav_thread.daemon = True
    nav_thread.start()

    while not done.is_set():


        time.sleep(0.1)
    
    # If sucess assign last ros time
    if sucess:
        rospy.loginfo("All goals processed.")
    else:
        rospy.loginfo("Failed trial.")
    
    trialtime = 0.0

    return sucess, trialtime


def send_waypoints(stop, done):
    """
    This function sends a sequence of navigation goals to a robot.
    Output reward of trial in form of simulation time.
    """

    rospy.wait_for_service('router')

    goal_list = [
        {
            'position': {'x': 16.67, 'y': 2.76, 'z': 0.0},
            'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': -0.7} #BASE
        },
        {
            'position': {'x': 7.2, 'y': 2.79, 'z': 0.0},
            'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.99} #STOP1
        },
        {
            'position': {'x': 7.2, 'y': 6.69, 'z': 0.0},
            'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': -0.7} #STOP2
        },
        {
            'position': {'x': 1.444, 'y': 2.547, 'z': 0.0},
            'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.99} #STOP3
        },
        {
            'position': {'x': 16.67, 'y': 2.76, 'z': 0.0},
            'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': -0.7} #BACK TO BASE
        }
    ]
    
    try:
        send_waypoint = rospy.ServiceProxy('router', WaypointSender)

        
        for goal_data in goal_list:
            if stop.is_set() == False:

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
        
        done.set()

    except rospy.ServiceException as e:
        print("Error - couldn't get spawn_box service: %s" % e)    

    
def reset_gazebo():
    rospy.wait_for_service('/gazebo/reset_simulation')
    try:
        reset_sim = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
        reset_sim()  # Llama al servicio para reiniciar la simulación
        print("World reseted!.")
    except rospy.ServiceException as e:
        print("Error reseting world: %s" % e)

def delete_model(model_name):
    # Esperar hasta que el servicio delete_model esté disponible
    rospy.wait_for_service('/gazebo/delete_model')
    
    try:
        # Crear un cliente para el servicio delete_model
        delete_model_service = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
        
        # Llamar al servicio con el nombre del modelo a eliminar
        response = delete_model_service(model_name)
        
        if response.success:
            rospy.loginfo(f"Model '{model_name}' removed sucesfully.")
        else:
            rospy.logwarn(f"Unable to remove the model '{model_name}': {response.status_message}")
    
    except rospy.ServiceException as e:
        rospy.logerr(f"Error calling Gazebo delete model service: {e}")

# Process msg from topic /gazebo/link_states
def gazebo_callback(msg):
  global pose_dic
  for name, pose in zip(msg.name, msg.pose):
    if name == "mir::base_footprint" or name.startswith("Box_"):
      #pose_dic{name}=pose
      rospy.loginfo("Nombre: %s, Posición: (%f, %f, %f)", name, pose.position.x, pose.position.y, pose.position.z)
      # print("#########################################################")



if __name__ == '__main__':
    # Setup
    rospy.init_node('box_client')

    rospy.Subscriber('/gazebo/link_states', LinkStates, callback_mir_pose)

    # Init Spawn and Delete Box Services:
    rospy.wait_for_service('spawn_box')
    spawn_box = rospy.ServiceProxy('spawn_box', SpawnBox)
    delete_box = rospy.ServiceProxy('delete_box', DeleteBox)
    set_param_srv = rospy.ServiceProxy('set_param', SetParam)

    ############## TEST SET PARAM SERVICE ###########################
    # Set MAX robot params  
    try:
        print('Attemp to set params')
        mir_params = SetParamRequest(
            max_speed_xy =  0.8,
            max_vel_x =  0.8,
            acc_lim_x = 1.5,
            decel_lim_x = 1.5,
            max_vel_theta = 1.0
        )

        set_param_srv(mir_params)
    except rospy.ServiceException as e:
        print("Error - couldn't get spawn_box service: %s" % e)

        

    ############## TEST SPAWN BOXES SERVICE #########################

    n_boxes = 10
    length = 0.2
    width = 0.2
    height = 0.2

    # Generate boxes name:
    boxes_id = ["Box_"+str(i) for i in range(n_boxes)]
    
    # Compute poses for boxes:
    poses = boxes_placement(n_boxes, width, length, height)
    
    # Spawn Boxes
    req = SpawnBoxRequest(
        boxes_id = boxes_id,
        mass = 5,
        length = 0.2,
        width = 0.2,
        height = 0.2,
        poses = poses
        )

    spawn_box(req)

    # Navigation - simulation trial
    rospy.loginfo(f"Wait while navegation happening...")
    sucess, trial_time = navigation_routine()
    
############## TEST NAVIGATION #########################
# # Define the list of goals with position and orientation
#   goals = [
#     {
#         'position': {'x': 16.67, 'y': 2.76, 'z': 0.0},
#         'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': -0.7} #BASE
#     },
#     {
#         'position': {'x': 7.2, 'y': 2.79, 'z': 0.0},
#         'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.99} #STOP1
#     },
#     {
#         'position': {'x': 7.2, 'y': 6.69, 'z': 0.0},
#         'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': -0.7} #STOP2
#     },
#     {
#         'position': {'x': 1.444, 'y': 2.547, 'z': 0.0},
#         'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.99} #STOP3
#     },
#     {
#         'position': {'x': 16.67, 'y': 2.76, 'z': 0.0},
#         'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': -0.7} #BACK TO BASE
#     }
#     ]

#   rospy.loginfo(f"Wait while navegation happening...")
#   arm_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
#   arm_client.wait_for_server()   # Lock the code

#   navigation_routine(goals, arm_client)
  
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

    
