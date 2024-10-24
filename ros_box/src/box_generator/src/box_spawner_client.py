""""
This service client script is used to test the SpawnBox service
"""

import rospy
from box_generator.srv import SpawnBox, SpawnBoxRequest, DeleteBox, DeleteBoxRequest
from gazebo_msgs.srv import SpawnModel, DeleteModel
from std_srvs.srv import Empty
from geometry_msgs.msg import Pose, Quaternion
from gazebo_msgs.msg import LinkStates 
import tf.transformations as tft
import random
import math


################## GAZEBO UTILS ############################
def reset_gazebo():
    rospy.wait_for_service('/gazebo/reset_simulation')
    try:
        reset_sim = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
        reset_sim()  # Llama al servicio para reiniciar la simulación
        print("World reseted!.")
    except rospy.ServiceException as e:
        print("Error reseting world: %s" % e)


if __name__ == '__main__':
  rospy.init_node('box_spawner')

  # Init Spawn and Delete Box Services:
  rospy.wait_for_service('spawn_box')
  spawn_box = rospy.ServiceProxy('spawn_box', SpawnBox)
  delete_box = rospy.ServiceProxy('delete_box', DeleteBox)

  n_boxes = 3
  
  # Generate boxes name:
  boxes_id = ["Box_"+str(i) for i in range(n_boxes)]
  
  # Spawn Boxes
  req = SpawnBoxRequest(
    boxes_id = boxes_id,
    mass = 5,
    length = 0.2,
    width = 0.2,
    height = 0.2
    )

  spawn_box(req)

  # Delete boxes:
  print('----> Hit enter to delete models.')
  a = input()

  req = DeleteBoxRequest(
     boxes_id = boxes_id
  )
  delete_box(req)
  
  
  print('----> Hit enter to reset the world.')
  a = input()
  reset_gazebo()

    
