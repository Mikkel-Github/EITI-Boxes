import math
import uuid

class Orientation:
    width: float
    length: float
    height: float

    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

class Point:
    x: float
    y: float
    z: float

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

MAX_HEIGHT = 200 # meters
MAX_WIDTH = 60
MAX_LENGTH = 80
MAX_WEIGHT = 100000 # in grams

class RobotSettings:
    def __init__(self, acceleration=1.5, deacceleration=-1.5, speed=1.2, velocity=1.5, velocity_theta=1.5):
        self.acceleration = acceleration
        self.deacceleration = deacceleration
        self.speed = speed
        self.velocity = velocity
        self.velocity_theta = velocity_theta

    def lower_values(self):
        self.acceleration -= 0.1
        self.deacceleration -= 0.1
        self.speed -= 0.1
        self.velocity -= 0.1
        self.velocity_theta -= 0.1

class Layout:
    def __init__(self, positions, orientation, mass, robot_settings: RobotSettings):
        # Generate a unique id for this layout so if multiple simulations are running, they can provide the results for a specific layout
        self.id = str(uuid.uuid4())
        self.positions = positions
        self.orientation = orientation
        self.mass = mass
        self.robot_settings = robot_settings

# Class for the simulation to send to this algorithm:
class RobotMessage:
    def __init__(self, layout: Layout, result_success=False, result_time=0):
        self.layout = layout
        self.result_success = result_success
        self.result_time = result_time

class RunHandler:
    def __init__(self):
        self.runs = []

    def add_new_run(self, layout: Layout):
        self.runs.append(layout)

    def handle_result(self, layout_id: str, robot_message: RobotMessage):
        for run in self.runs:
            if run.id == layout_id:
                if robot_message.result_success == True:
                    # The run was success, go to the next configuration
                    pass
                else:
                    run.robot_settings
                    



def get_all_orientations(width, length, height):
    orientation_dict = {}

    # Case when all dimensions are equal
    if width == length == height:
        orientation_dict["orientation_1"] = Orientation(width, length, height)  # Only one configuration for a cube
    
    # Case when 2 dimensions are equal
    elif width == length:
        orientation_dict["orientation_1"] = Orientation(width, length, height)
        orientation_dict["orientation_2"] = Orientation(width, height, length)
        orientation_dict["orientation_3"] = Orientation(height, width, length)

    elif length == height:
        orientation_dict["orientation_1"] = Orientation(width, length, height)
        orientation_dict["orientation_2"] = Orientation(length, height, width)
        orientation_dict["orientation_3"] = Orientation(height, width, length)

    elif width == height:
        orientation_dict["orientation_1"] = Orientation(width, length, height)
        orientation_dict["orientation_2"] = Orientation(length, width, height)
        orientation_dict["orientation_3"] = Orientation(height, width, length)
    
    # General case when all dimensions are different
    else:
        orientation_dict["orientation_1"] = Orientation(width, length, height)
        orientation_dict["orientation_2"] = Orientation(width, height, length)
        orientation_dict["orientation_3"] = Orientation(length, width, height)
        orientation_dict["orientation_4"] = Orientation(length, height, width)
        orientation_dict["orientation_5"] = Orientation(height, width, length)
        orientation_dict["orientation_6"] = Orientation(height, length, width)

    # Check constrains:
    """ orientation_dict = {
        key: orient for key, orient in orientation_dict.items()
        if orient.width <= MAX_WIDTH and orient.length <= MAX_LENGTH and orient.height <= MAX_HEIGHT
    } """

    return orientation_dict

def get_standard_orientations(width, length, height):
    orientation_dict = []

    if width == length:
        orientation_dict["standard_orientation_1"] = Orientation(width, length, height)
    else:
        orientation_dict["standard_orientation_1"] = Orientation(width, length, height)
        orientation_dict["standard_orientation_2"] = Orientation(length, width, height)

    orientation_dict = {
        key: orient for key, orient in orientation_dict.items()
        if orient.width <= MAX_WIDTH and orient.length <= MAX_LENGTH and orient.height <= MAX_HEIGHT
    }

    return orientation_dict

def fill(num_boxes, box_width, box_length, max_boxes_width, max_boxes_length, z, mir_width, mir_length):
    grid_y = math.ceil(num_boxes/max_boxes_width)
    grid_x = math.ceil(num_boxes/max_boxes_length)
    remaining_boxes = num_boxes
    positions = []
    for i in range(grid_y):
        for j in range(grid_x):
            x = (grid_x * box_width + (box_width/2)) + (mir_width/2) - (grid_x/2) * box_width
            y = (grid_y * box_length + (box_length/2)) + (mir_length/2) - (grid_y/2) * box_length
            positions.append(Point(x, y, z))
            remaining_boxes -= 1
            if remaining_boxes == 0:
                return positions
    return positions

def fill_new(num_boxes, box_width, box_length, box_height, max_boxes_width, max_boxes_length, box_weight):
    positions = []
    total_weight = 0
    remaining_boxes = num_boxes
    z = box_height / 2

    # While there is still boxes to be placed:
    while remaining_boxes > 0:
        # Go through the grid of potential places
        for y in range(max_boxes_length): 
            for x in range(max_boxes_width):
                xx = ((x * box_width) + (box_width/2)) + (MAX_WIDTH/2) - ((x/2) * box_width)
                yy = ((y * box_length) + (box_length/2)) + (MAX_LENGTH/2) - ((y/2) * box_length)
                
                positions.append(Point(xx, yy, z))
                
                remaining_boxes -= 1
                if(remaining_boxes <= 0):
                    print("No more boxes to place limit reached")
                    return positions

                total_weight += box_weight

                # If adding one more box makes it overweight, then stop
                if total_weight + box_weight > MAX_WEIGHT:
                    print("Weight limit reached")
                    return positions

        # When a layer is filled an there is still boxes remaining, go up a layer
        z += box_height

        # If going up one more layer, goes over the maximum height, then stop
        if(z + (box_height / 2) > MAX_HEIGHT): 
            print("Height limit reached")
            return positions
    
    print("No limit reached")
    return positions

def get_layouts(num_boxes, width, length, height, box_weight, fragile):
    # if the boxes contain fragile content, then don't rotate the boxes:
    if fragile:
        orientations = get_standard_orientations(width, length, height)
    else: 
        orientations = get_all_orientations(width, length, height)

    # Generate a list that will contain all the possible orientations
    layouts = []
    for o in orientations.keys():
        orientation = orientations[o]
        # Calculate how many boxes fit per layer
        boxes_per_length = int(MAX_LENGTH // orientation.length)
        boxes_per_width = int(MAX_WIDTH // orientation.width)

        boxes_per_layer = boxes_per_length * boxes_per_width
        max_boxes = boxes_per_layer * int(MAX_HEIGHT // orientation.height)
        print(f"Boxes per length: {boxes_per_length}, boxes per width: {boxes_per_width}, boxes per layer: {boxes_per_layer}, max boxes (could be lower due to weight, height or amount of boxes): {max_boxes}")

        # Generate all the positions for 
        positions = fill_new(num_boxes, orientation.width, orientation.length, orientation.height, boxes_per_width, boxes_per_length, box_weight)
        print(f"Generated {len(positions)} positions")

        # When the simulation returns a result, some of these parameters will be lowered and tried again.
        # Empty RobotSettings() will make it default to maximum values
        robot_settings = RobotSettings()

        # This message will contain one way of positioning the boxes, the orientation, the weight, and the settings for the robot.
        layout = Layout(positions, orientation, box_weight, robot_settings)

        layouts.append(layout)

    return layouts

# Receive from website:
#   number of boxes
#   size of a box
#   if the content is fragile

def Setup(num_boxes, width, length, height, box_weight, fragile):
    # Generate all possible layouts
    layouts = get_layouts(num_boxes, width, length, height, box_weight, fragile)
    print(f"Generated {len(layouts)} layouts")

import time
start_time = time.time()
Setup(100, 10, 20, 30, 10, False)
print("--- %s seconds ---" % (time.time() - start_time))