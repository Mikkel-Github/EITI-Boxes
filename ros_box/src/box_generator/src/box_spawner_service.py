
import rospy
from gazebo_msgs.srv import SpawnModel, DeleteModel
from geometry_msgs.msg import Pose, Point, Quaternion
from gazebo_msgs.msg import LinkStates
from box_generator.srv import SpawnBox, SpawnBoxResponse, DeleteBox, DeleteBoxResponse
import numpy as np
import tf.transformations as tr
import math

pose_mir = None

# Global parameters: Defined for MIR100
MAX_HEIGHT = 2 # meters
MAX_WIDTH = 0.60
MAX_LENGHT = 0.80
MAX_N_CONFIGURATIONS = 100

############ CALL BACK: RECEIVE MIR POSITION ##########################
def gazebo_callback(msg):
    global pose_mir
    for name, pose in zip(msg.name, msg.pose):
        if name == "mir::base_footprint":
            pose_mir = pose

        #rospy.loginfo("Nombre: %s, Posición: (%f, %f, %f)", name, pose.position.x, pose.position.y, pose.position.z)

############# SERVICE: SPAWN BOXES ####################

def spawn_boxes_service(req):    
    
    assert req.width < MAX_WIDTH, "[WARNING] Boxes width exceed MIR width! Service stop."
    assert req.length < MAX_LENGHT, "[WARNING] : Boxes length exceed MIR length! Service stop."
    assert req.height < MAX_WIDTH, "[WARNING] : Boxes heigth exceed MIR heigth! Service stop."

    n_boxes = len(req.boxes_id)

    # Determine boxes position:
    poses = simple_boxes_placement(req)
    # TODO: Script to arange the boxes in a determined shape
    
    try:
        for i in range(n_boxes):
          box_id = req.boxes_id[i]
          spawn_single_box(req, box_id, poses[i])
        return SpawnBoxResponse(True, f"Done!")
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return SpawnBoxResponse(False, str(e))
    
def spawn_single_box(req, box_id, pose):

    # Generate SDF model:
    model_name = box_id
    mass = req.mass
    length = req.length
    width = req.width
    height = req.height
    sdf_content = generate_sdf_cardboard(model_name, mass, length, width, height)

    rospy.wait_for_service('/gazebo/spawn_sdf_model')
    spawn_model = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
    spawn_model(model_name, sdf_content, '', pose, 'world')
    rospy.loginfo(f"Model '{model_name}' spawned successfully")

################# BOXES PLACEMENT ####################
def simple_boxes_placement(req):
    # NOTE: This script create a matrix of ros Pose where to place the boxes

    # Dimension of arrangement matrix:
    max_num_box_width = int(MAX_WIDTH / req.width)
    max_num_box_length = int(MAX_LENGHT / req.length)
    max_num_box_height = int(MAX_HEIGHT / req.height)

    max_capacity = max_num_box_height*max_num_box_length*max_num_box_width # Maximun number of boxes that can be carried
    max_boxes_per_layer = max_num_box_width*max_num_box_length

    print("Max capacity: ", max_capacity)
    
    if len(req.boxes_id) > max_capacity:
      # TODO: If n boxes exceed the max capacity do something
      pass

    # Compute Center of Gravity stack of boxes:
    cog_width = (req.width*max_num_box_width)/2
    cog_length = (req.length*max_num_box_length)/2
    translation_cog_origin = np.array([cog_length, cog_width, 0])
    
    # Translation and rotation matrix from MIR base pose
    global pose_mir
  
    translation_origin_mir = [pose_mir.position.x, pose_mir.position.y, pose_mir.position.z + 0.2]
    quaternion = [pose_mir.orientation.x, pose_mir.orientation.y, pose_mir.orientation.z, pose_mir.orientation.w]
    rotation_matrix = tr.quaternion_matrix(quaternion)[0:3,0:3]

    # Define position matrix:
    pose_list = []
    cont = 0
    break_all = False
    # Layer dimension:
    for k in range(max_num_box_height):
      boxes_left = len(req.boxes_id) - cont
      print(boxes_left)
      if boxes_left < max_boxes_per_layer:
        num_width_this_layer = max_num_box_width
        num_length_this_layer = math.ceil(boxes_left/num_width_this_layer)
        
      else:
        num_width_this_layer = max_num_box_width
        num_length_this_layer = max_num_box_length
      # Layer CoG:
      cog_width = (req.width*num_width_this_layer)/2
      cog_length = (req.length*num_length_this_layer)/2
      translation_cog_origin = np.array([cog_length, cog_width, 0])
      
      for j in range(num_width_this_layer):
        for i in range(num_length_this_layer):
          if cont < len(req.boxes_id) and cont < max_capacity:
            cont = cont + 1

            # Compute single box CoG:
            x = i*req.length + req.length/2 
            y = j*req.width + req.width/2 
            z = k*req.height + req.height/2 
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
            pose.orientation = pose_mir.orientation

            print('Pose box ', cont, ':', pose)
            pose_list.append(pose)
          else:
            break_all = True
            break
        if break_all:
           break
      if break_all:
         break
        
                    
    # poses = []
    # for n in range(req.n_boxes):
    #     pose = Pose()
    #     pose.position.x = pose_mir.position.x
    #     pose.position.y = pose_mir.position.y
    #     pose.position.z = pose_mir.position.z + 0.3 + 0.2*n
    #     pose.orientation = pose_mir.orientation

    #     poses.append(pose)

    return pose_list

############ SERVICE: DELETE BOXES #####################
#       
def delete_box_service(req):
    boxes_id_list = req.boxes_id
    boxes_id_list.reverse()
    for box_id in boxes_id_list:
        rospy.loginfo(f"Received request to delete model: {box_id}")
        success, message = delete_model(box_id)
    
    if success:
        return DeleteBoxResponse(success=True, message="Models deleted successfully")
    else:
        return DeleteBoxResponse(success=False, message=message)
    
def delete_model(model_name):
    # Esperar hasta que el servicio delete_model esté disponible
    rospy.wait_for_service('/gazebo/delete_model')
    
    try:
        # Crear un cliente para el servicio delete_model
        delete_model_service = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
        
        # Llamar al servicio con el nombre del modelo a eliminar
        response = delete_model_service(model_name)
        
        if response.success:
            rospy.loginfo(f"Model '{model_name}' removed successfully.")
            return True, "Model deleted successfully"
        else:
            rospy.logwarn(f"Unable to remove the model '{model_name}': {response.status_message}")
            return False, response.status_message
    
    except rospy.ServiceException as e:
        rospy.logerr(f"Error calling Gazebo delete model service: {e}")
        return False, str(e)

############ GENERATE BOX MODEL ##################

def generate_sdf(model_name, mass, length, width, height):
  # Generar el contenido URDF
  sdf_content = f"""
  <?xml version='1.0'?>
  <sdf version="1.4">
    <model name="{model_name}">
      <pose>0 0 {height / 2} 0 0 0</pose>
      <static>0</static>
      <link name="link">
        <inertial>
          <mass>{mass}</mass>
          <inertia>
            <ixx>{(1/12) * mass * (width**2 + height**2)}</ixx>
            <iyy>{(1/12) * mass * (length**2 + height**2)}</iyy>
            <izz>{(1/12) * mass * (length**2 + width**2)}</izz>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyz>0</iyz>
          </inertia>
          <pose>0 0 0 0 -0 0</pose>
        </inertial>
        <collision name="collision">
          <geometry>
            <box>
              <size>{length} {width} {height}</size>
              <scale>1 1 1</scale>
            </box>
          </geometry>
          <max_contacts>50</max_contacts>
          <surface>
              <friction>
              <ode>
                  <mu>0.9</mu>
                  <mu2>0.9</mu2>
              </ode>
              <bullet>
                <friction1>0.3</friction1>
                <friction2>0.3</friction2>
              </friction>
              <contact>
                <ode/>
              </contact>
              
          </surface>
        </collision>
        <visual name="visual">
          <geometry>
            <box>
              <size>{length} {width} {height}</size>
            </box>
          </geometry>
          <material>
              <ambient>0.6 0.4 0.2 1</ambient>  <!-- Ambient color: light brown -->
              <diffuse>0.7 0.5 0.3 1</diffuse>  <!-- Diffuse color: cardboard brown -->
              <specular>0.1 0.1 0.1 1</specular> <!-- Specular highlights: slight shine -->
              <emissive>0 0 0 1</emissive>       <!-- Emissive color: no self-illumination -->
          </material>
        </visual>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
    </model>
  </sdf>
  """
  
  return sdf_content

def generate_sdf_cardboard(model_name, mass, length, width, height):
  # Generar el contenido URDF
  sdf_content = f"""
  <?xml version='1.0'?>
  <sdf version="1.4">
    <model name="{model_name}">
      <pose>0 0 {height / 2} 0 0 0</pose>
      <static>0</static>
      <link name="link">
        <inertial>
          <mass>{mass}</mass>
          <density>500</density>
          <inertia>
            <ixx>{(1/12) * mass * (width**2 + height**2)}</ixx>
            <iyy>{(1/12) * mass * (length**2 + height**2)}</iyy>
            <izz>{(1/12) * mass * (length**2 + width**2)}</izz>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyz>0</iyz>
          </inertia>
          <pose>0 0 0 0 -0 0</pose>
        </inertial>

        <collision name="collision">
          <max_contacts>50</max_contacts>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <box>
              <size>{length} {width} {height}</size>
              <scale>1 1 1</scale>
            </box>
          </geometry>
          
          <surface>
              <contact>
                <ode/>
              </contact>
              <bounce/>
              <friction>
              <ode>
                  <mu>0.9</mu>
                  <mu2>0.9</mu2>
              </ode>
              </friction>
          </surface>
        </collision>
        <visual name="visual">
          <geometry>
            <box>
              <size>{length} {width} {height}</size>
            </box>
          </geometry>
          <material>
              <ambient>0.6 0.4 0.2 1</ambient>  <!-- Ambient color: light brown -->
              <diffuse>0.7 0.5 0.3 1</diffuse>  <!-- Diffuse color: cardboard brown -->
              <specular>0.1 0.1 0.1 1</specular> <!-- Specular highlights: slight shine -->
              <emissive>0 0 0 1</emissive>       <!-- Emissive color: no self-illumination -->
          </material>
        </visual>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
    </model>
  </sdf>
  """
  
  return sdf_content


# <script>
#   <name>Gazebo/Grey</name>
#   <uri>file://media/materials/scripts/gazebo.material</uri>
# </script>

if __name__ == '__main__':
    rospy.init_node('box_spawner_service')
    
    # Subscribe to the Gazebo links state topic
    rospy.Subscriber('/gazebo/link_states', LinkStates, gazebo_callback)
  
    # Crear los servidores de servicios
    spawn_box_srv = rospy.Service('spawn_box', SpawnBox, spawn_boxes_service)

    # Servicio para eliminar cajas
    delete_service = rospy.Service('delete_box', DeleteBox, delete_box_service)

    rospy.loginfo("Ready to spawn and delete boxes.")
    rospy.spin()
