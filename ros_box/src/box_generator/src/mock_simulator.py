import random
import time
import uuid

class Layout:
    def __init__(self, positions, orientation, mass, robot_settings):
        # Generate a unique id for this layout so if multiple simulations are running, they can provide the results for a specific layout
        self.id = str(uuid.uuid4())
        self.positions = positions
        self.orientation = orientation
        self.mass = mass
        self.robot_settings = robot_settings

class RobotSettings:
    def __init__(self, acceleration=1.5, deacceleration=-1.5, speed=1.2, velocity=1.5, velocity_theta=1.5):
        self.acceleration = acceleration
        self.deacceleration = deacceleration
        self.speed = speed
        self.velocity = velocity
        self.velocity_theta = velocity_theta

class RobotMessage:
    def __init__(self, layout, result_success=False, result_time=0):
        self.layout = layout
        self.result_success = result_success
        self.result_time = result_time

def mock_simulator(layout: Layout) -> RobotMessage:
    """
    Mock the robot simulation. This function simulates a robot's movement based on the provided layout.
    The simulation will take around 40 seconds with a random variation and may fail based on the layout's robot settings.
    """
    # Initial setup
    base_simulation_time = 10  # Base time for simulation in seconds
    random_variation = random.uniform(-5, 5)  # Random variation in the range of -5 to +5 seconds
    total_simulation_time = base_simulation_time + random_variation

    # Calculate failure chance based on robot settings (the closer to default values, the higher the failure chance)
    failure_chance = 0.1  # Default failure chance for random settings
    if (layout.robot_settings.acceleration == 1.5 and
        layout.robot_settings.deacceleration == -1.5 and
        layout.robot_settings.speed == 1.2 and
        layout.robot_settings.velocity == 1.5 and
        layout.robot_settings.velocity_theta == 1.5):
        failure_chance = 0.6  # Higher failure chance if robot settings are at the default values

    # Random chance for failure
    result_success = random.random() > failure_chance  # Simulate success or failure
    result_time = total_simulation_time if result_success else random.uniform(5, total_simulation_time - 5)

    # Simulate the robot "doing work" for the specified time (just for simulation, can be removed if unnecessary)
    time.sleep(result_time)

    # Return the result as a RobotMessage
    return RobotMessage(layout=layout, result_success=result_success, result_time=result_time)

# Example usage
#robot_settings = RobotSettings(acceleration=1.5, deacceleration=-1.5, speed=1.2, velocity=1.5, velocity_theta=1.5)
#layout = Layout(positions=[0, 0], orientation=90, mass=50, robot_settings=robot_settings)

#robot_message = mock_simulator(layout)
#print(f"Simulation Result: Success={robot_message.result_success}, Time={robot_message.result_time:.2f}s")
