import rospy
from gazebo_msgs.srv import SpawnModel, DeleteModel
from geometry_msgs.msg import Pose, Quaternion
from gazebo_msgs.msg import LinkStates
from box_generator.srv import SpawnBox, SpawnBoxResponse, DeleteBox, DeleteBoxResponse

pose_mir = None

############ CALL BACK: RECEIVE MIR POSITION ##########################
def gazebo_callback(msg):
    global pose_mir
    for name, pose in zip(msg.name, msg.pose):
        if name == "mir::base_footprint":
            pose_mir = pose

        #rospy.loginfo("Nombre: %s, Posición: (%f, %f, %f)", name, pose.position.x, pose.position.y, pose.position.z)

############# SERVICE: SPAWN BOXES ####################

def spawn_boxes_service(req):    
    n_boxes = len(req.boxes_id)

    # Determine boxes position:
    poses = simple_boxes_placement(n_boxes)
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
    sdf_content = generate_urdf(model_name, mass, length, width, height)

    rospy.wait_for_service('/gazebo/spawn_sdf_model')
    spawn_model = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
    spawn_model(model_name, sdf_content, '', pose, 'world')
    rospy.loginfo(f"Model '{model_name}' spawned successfully")

def simple_boxes_placement(n_boxes):
    # Simple script to make a pile of boxes
    global pose_mir

    poses = []
    for n in range(n_boxes):
        pose = Pose()
        pose.position.x = pose_mir.position.x
        pose.position.y = pose_mir.position.y
        pose.position.z = pose_mir.position.z + 0.3 + 0.2*n
        pose.orientation = pose_mir.orientation

        poses.append(pose)

    return poses

############ SERVICE: DELETE BOXES #####################
#       
def delete_box_service(req):
    boxes_id = req.boxes_id

    for n in range(len(boxes_id)):
        rospy.loginfo(f"Received request to delete model: {boxes_id[n]}")
        success, message = delete_model(boxes_id[n])
    
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

def generate_urdf(model_name, mass, length, width, height):
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
              <contact>
              <ode/>
              </contact>
              <bounce/>
              <friction>
              <ode>
                  <mu>0.25</mu>
                  <mu2>0.2</mu2>
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
              <script>
                  <name>Gazebo/Grey</name>
                  <uri>file://media/materials/scripts/gazebo.material</uri>
              </script>
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
