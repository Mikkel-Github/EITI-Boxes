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

    
