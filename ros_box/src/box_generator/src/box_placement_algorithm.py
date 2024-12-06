import math
import uuid

from mock_simulator import mock_simulator

from mqtt_publisher import announce_best_run, announce_orientation_evaluation

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

    def lower_values(self) -> bool:
        self.acceleration -= 0.1
        self.deacceleration -= 0.1
        self.velocity -= 0.1
        self.velocity_theta -= 0.1

        if self.acceleration < 0.8:
            return False
        return True

class Result:
    def __init__(self, success, time, boxes):
        self.success = success
        self.time = time
        self.boxes = boxes
        self.score = self.calculate_score()

    def calculate_score(self) -> int:
        if self.success is False:
            return -1
        
        # more boxes moved gives higher score, higher time gives lower score
        result = self.boxes - self.time

        if result < 0:
            result = 0

        return result
    
    def get_score(self) -> int:
        return self.score

class Layout:
    def __init__(self, positions, orientation, mass, robot_settings: RobotSettings):
        # Generate a unique id for this layout so if multiple simulations are running, they can provide the results for a specific layout
        self.id = str(uuid.uuid4())
        self.positions = positions
        self.orientation = orientation
        self.mass = mass
        self.robot_settings = robot_settings
        self.result = None
        self.runs = 0

    def set_results(self, result: Result):
        self.result = result

    def increment_run(self):
        self.runs += 1

    def get_runs(self) -> int:
        return self.runs
    
# Class for the simulation to send to this algorithm:
class RobotMessage:
    def __init__(self, layout: Layout, result_success=False, result_time=0):
        self.layout = layout
        self.result_success = result_success
        self.result_time = result_time

class RunHandler:
    def __init__(self):
        self.runs = []

    def has_runs(self) -> bool:
        return len(self.runs) > 0

    def add_new_run(self, layout: Layout):
        self.runs.append(layout)

    def get_first_run(self) -> Layout:
        return self.runs[0]

    def handle_result(self, robot_message: RobotMessage) -> Layout:
        go_to_next_run = False
        for run in self.runs:
            if go_to_next_run:
                print("go to next run")
                return run
            
            if run.id == robot_message.layout.id:
                run.increment_run()
                if robot_message.result_success == True:
                    print("finished run")

                    run.set_results(Result(True, robot_message.result_time, len(run.positions)))

                    announce_orientation_evaluation(run.get_runs())
                    # The run was success, go to the next configuration
                    go_to_next_run = True
                else:
                    # Lower the robot parameters, but if the parameters are too low, go to the next run instead
                    should_run_again = run.robot_settings.lower_values()
                    if should_run_again:
                        print("run again")
                        return run
                    
                    # Set the run to be a failure
                    run.set_results(Result(False, 0, 0))
                    
                    go_to_next_run = True 
    
    def get_best_run(self) -> Layout:
        best_run = None
        for run in self.runs:
            if best_run == None:
                best_run = run
            elif run.result.get_score() > best_run.result.get_score():
                best_run = run

        return best_run
                

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

class Algorithm:
    def __init__(self): 
        self.run_handler = RunHandler()

    def Setup(self, num_boxes, width, length, height, box_weight, fragile):
        # Generate all possible layouts
        layouts = get_layouts(num_boxes, width, length, height, box_weight, fragile)
        print(f"Generated {len(layouts)} layouts")

        for layout in layouts:
            self.run_handler.add_new_run(layout)

        len_layouts = len(layouts)
        return len_layouts
        

    def EvaluateRun(self, robot_message: RobotMessage):
        print("Evaluate run: " + robot_message.layout.id)
        # run_to_perform could be the same run with lower robot parameters or the next layout
        run_to_perform = self.run_handler.handle_result(robot_message)
        if run_to_perform is None:
            return
        
        self.EvaluateRun(mock_simulator(run_to_perform))
        

    def StartSimulation(self):
        print("Start Simulation")
        if self.run_handler.has_runs():
            print("has runs")
            # This will keep calling EvaluateRun until there are no more runs left
            self.EvaluateRun(mock_simulator(self.run_handler.get_first_run()))

        # There are no more runs left, now get the best run
        best_run = self.run_handler.get_best_run()
        announce_best_run(best_run)


# import time
# start_time = time.time()
# Setup(100, 10, 20, 30, 10, False)
# print("--- %s seconds ---" % (time.time() - start_time))