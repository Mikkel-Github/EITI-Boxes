import math

class Orientation:
    width: float
    length: float
    height: float

class Point:
    x: float
    y: float
    z: float

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

def get_layouts(num_boxes, width, length, height, mir_width, mir_length, max_height, max_weight, box_weight, fragile):
    if fragile:
        orientations = get_standard_orientations(width, length, height)
    else: 
        orientations = get_all_orientations(width, length, height)

    layouts = []
    for orientation in orientations.values():
        # Calculate how many boxes fit per layer
        boxes_per_length = int(mir_length // orientation.length)
        boxes_per_width = int(mir_width // orientation.width)
        boxes_per_layer = boxes_per_length * boxes_per_width
        layout = {}
        if(boxes_per_layer > num_boxes):
            positions = fill(num_boxes, width, length, boxes_per_width, boxes_per_length, height/2, mir_width, mir_length)
            layout["positions"] = positions
            layout["acceleration"] = 1.5
            layout["deaccceleration"] = -1.5
            layout["speed"] = 1.2
            layout["velocity"] = 1.5
            layout["velocity_theta"] = 1.5
            layout["results_success"] = False
            layout["results_time"] = 0
            layouts.append(layout)
            