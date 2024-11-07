import rospy
from gazebo_msgs.srv import SpawnModel, DeleteModel
from geometry_msgs.msg import Pose, Quaternion
from gazebo_msgs.msg import LinkStates
from box_generator.srv import SpawnBox, SpawnBoxResponse, DeleteBox, DeleteBoxResponse
from typing import List
import numpy as np

# Global parameters: Defined for MIR100
MAX_HEIGHT = 20 # cm
MAX_WIDTH = 60
MAX_LENGHT = 80
MAX_N_CONFIGURATIONS = 100

class Orientation:
    width: float
    length: float
    height: float

class Point:
    x: float
    y: float
    z: float

class CellCage():
    def __init__(self, box_dim: Orientation, n_boxes: int):
        self.box_dim = box_dim
        self.n_boxes = n_boxes

        self.matrix_width = int(MAX_WIDTH / box_dim.width)
        self.matrix_length = int(MAX_LENGHT / box_dim.length)
        self.matrix_height = int(MAX_HEIGHT / box_dim.height)

        # Define position matrix:
        self.position_matrix = np.empty((self.matrix_width, self.matrix_length, self.matrix_height), dtype=Point)
        for i in range(self.matrix_width):
            for j in range(self.matrix_length):
                for k in range(self.matrix_height):
                    # Potential box position:
                    # TODO: Change poses so they start from the center of the platform to the edges
                    x = i*box_dim.width/2 + box_dim.width/2
                    y = j*box_dim.length/2 + box_dim.length/2
                    z = k*box_dim.height/2 + box_dim.height/2
                    self.position_matrix[i,j,k] = Point(x,y,z)

    def create_occupation_matrix(self):
        return np.array()
    
    def explore_configuration(self):
        occupation_matrix = np.zeros((self.matrix_width, self.matrix_length, self.matrix_height), dtype=bool)
        # TODO: Recursive function to explore all possible configurations starting from the center

def get_all_orientations(width, length, height):
    orientation_dict = {}

    # Case when all dimensions are equal
    if width == length == height:
        orientation_dict["orientation_1"] = Orientation(width=width, length=length, height=height)  # Only one configuration for a cube
    
    # Case when 2 dimensions are equal
    elif width == length:
        orientation_dict["orientation_1"] = Orientation(width=width, length=length, height=height)
        orientation_dict["orientation_2"] = Orientation(width=width, length=height, height=length)
        orientation_dict["orientation_3"] = Orientation(width=height, length=width, height=length)

    elif length == height:
        orientation_dict["orientation_1"] = Orientation(width=width, length=length, height=height)
        orientation_dict["orientation_2"] = Orientation(width=length, length=height, height=width)
        orientation_dict["orientation_3"] =Orientation(width=height, length=width, height=length)

    elif width == height:
        orientation_dict["orientation_1"] = Orientation(width=width, length=length, height=height)
        orientation_dict["orientation_2"] = Orientation(width=length, length=width, height=height)
        orientation_dict["orientation_3"] = Orientation(width=height, length=width, height=length)
    
    # General case when all dimensions are different
    else:
        orientation_dict["orientation_1"] = Orientation(width=width, length=length, height=height)
        orientation_dict["orientation_2"] = Orientation(width=width, length=height, height=length)
        orientation_dict["orientation_3"] = Orientation(width=length, length=width, height=height)
        orientation_dict["orientation_4"] = Orientation(width=length, length=height, height=width)
        orientation_dict["orientation_5"] = Orientation(width=height, length=width, height=length)
        orientation_dict["orientation_6"] = Orientation(width=height, length=length, height=width)

    # Check constrains:
    orientation_dict = {
        key: orient for key, orient in orientation_dict.items()
        if orient.width <= MAX_WIDTH and orient.length <= MAX_LENGHT and orient.height <= MAX_HEIGHT
    }

    return orientation_dict

def get_standard_orientations(width, length, height):
    orientation_dict = []

    if width == length:
        orientation_dict["standard_orientation_1"] = Orientation(width=width, length=length, height=height)
    else:
        orientation_dict["standard_orientation_1"] = Orientation(width=width, length=length, height=height)
        orientation_dict["standard_orientation_2"] = Orientation(width=length, length=width, height=height)

    orientation_dict = {
        key: orient for key, orient in orientation_dict.items()
        if orient.width <= MAX_WIDTH and orient.length <= MAX_LENGHT and orient.height <= MAX_HEIGHT
    }

    return orientation_dict


############# SERVICE: PLACE BOXES ####################

def place_boxes_service(req):    
    n_boxes = len(req.boxes_id)
    mass = req.mass
    length = req.length
    width = req.width
    height = req.height

    orientation_list = generate_orientations(length, width, height)

    for orientation in orientation_list:
        compute_configuration()
    
    # Determine boxes position:
    poses = simple_boxes_placement(n_boxes)
    # TODO: Script to arange the boxes in a determined shape

    for i in range(n_boxes):
        box_id = req.boxes_id[i]
        spawn_single_box(req, box_id, poses[i])
    
    try:
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
    sdf_content = generate_sdf(model_name, mass, length, width, height)

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

    




if __name__ == '__main__':
    rospy.init_node('box_placer_service')
  
    # Crear los servidores de servicios
    spawn_box_srv = rospy.Service('place_boxes', BoxPlacer, place_boxes_service)


    rospy.loginfo("Ready to spawn and delete boxes.")
    rospy.spin()
