import rospy
from gazebo_msgs.srv import SpawnModel, DeleteModel
from std_srvs.srv import Empty
from geometry_msgs.msg import Pose, Quaternion
import tf.transformations as tft
import random
import math

def generate_sdf(model_name, mass, length, width, height):
    # Generar el contenido SDF
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

def generate_sdf_bullet(model_name, mass, length, width, height):
    # Generar el contenido SDF
    sdf_content = f"""
    <?xml version='1.0'?>
    <sdf version="1.7">
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
          
          <!-- Configuración de colisiones y físicas con Bullet -->
          <collision name="collision">
            <geometry>
              <box>
                <size>{length} {width} {height}</size>
              </box>
            </geometry>
            <max_contacts>50</max_contacts>
            <surface>
                <contact>
                  <bullet>
                    <soft_contact>
                      <kp>50000</kp>  <!-- Rigidez del contacto -->
                      <kd>0.1</kd>    <!-- Amortiguación del contacto -->
                    </soft_contact>
                  </bullet>
                </contact>
                <friction>
                  <bullet>
                    <friction>
                      <mu>0.25</mu>  <!-- Coeficiente de fricción dinámico -->
                      <mu2>0.2</mu2>  <!-- Coeficiente de fricción en la segunda dirección -->
                    </friction>
                  </bullet>
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
          <enable_wind>1</enable_wind> <!-- Habilitar efectos del viento para mayor realismo -->
          <kinematic>0</kinematic>
        </link>
      </model>
    </sdf>
    """
    return sdf_content


def spawn_box(model_name, mass, length, width, height, x, y, z, roll, pitch, yaw):
    # TODO: Add material as parameter --> determine friction factor
    # TODO: Define topic /box_param_global with parameters shared by all the boxes (mass, dimension, etc) + number of boxes
    # TODO: Design engine to place the boxes. Boxes posese not received in /box_param_global

    sdf_content = generate_sdf(model_name, mass, length, width, height)

    # Convertir Euler a Cuaternión
    quat = tft.quaternion_from_euler(roll, pitch, yaw)
    
    # Crear objeto Pose
    pose = Pose()
    pose.position.x = x
    pose.position.y = y
    pose.position.z = z + height / 2  # Para asegurar que la caja quede sobre el suelo
    pose.orientation = Quaternion(*quat)  # Asignar cuaternión

    try:
        rospy.wait_for_service('/gazebo/spawn_sdf_model')
        spawn_model = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        spawn_model(model_name, sdf_content, '', pose, 'world')
        rospy.loginfo(f"Model '{model_name}' spawned successfully")
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

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


if __name__ == '__main__':
    rospy.init_node('box_spawner')
    n_boxes = 3
    
    x = [-0, 0, 0]
    y = [0, 0, 0]
    z = [0.35, 0.55, 0.75]
    roll = [0, 0, 0]
    pitch = [0, 0, 0]
    yaw = [0, 0, 0]

    id_list = []
    for i in range(n_boxes):
      box_id = 'Box_'+str(i)
      id_list.append(box_id)
      # x = random.uniform(-5, 5)
      # y = random.uniform(-5, 5)
      # z = random.uniform(-5, 5)
      # roll = random.uniform(-math.pi, math.pi)
      # pitch = random.uniform(-math.pi, math.pi)
      # yaw = random.uniform(-math.pi, math.pi)

      spawn_box(box_id, 5, 0.2, 0.2, 0.2,x[i],y[i],z[i],roll[i],pitch[i],yaw[i])

    # Delete boxes:
    print('----> Hit enter to delete models.')
    a = input()

    for id in id_list:
      delete_model(id)
    
    print('----> Hit enter to reset the world.')
    a = input()
    reset_gazebo()

      
