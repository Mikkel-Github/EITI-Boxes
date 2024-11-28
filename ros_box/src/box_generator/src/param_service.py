#!/usr/bin/env python3
import rospy

from dynamic_reconfigure.client import Client
from box_generator.srv import SetParam, SetParamResponse

# Service callback to handle requests
def handle_set_param(req):
    try:
        # Set up the client to connect to the DWBLocalPlanner's dynamic reconfigure server
        client = Client("/move_base_node/DWBLocalPlanner")

        # Prepare the new configuration dictionary from the request
        new_config = {
            'max_speed_xy': req.max_speed_xy,     #this setting must be change for the max vel to work - (DEFAULT: 0.8)
            'max_vel_x': req.max_vel_x,           # real max vel limit - (DEFAULT: 0.8)
            'acc_lim_x': req.acc_lim_x,           # acceleration upper limit - (DEFAULT: 1.5)
            'decel_lim_x': req.decel_lim_x,       # decel lower limit - (DEFAULT: 1.5)
            'max_vel_theta': req.max_vel_theta    # turn ratio.  - (DEFAULT: 1.0)
        }

        # Update configuration using dynamic reconfigure
        client.update_configuration(new_config)

        rospy.loginfo("Updated parameters: %s", new_config)
        return SetParamResponse(success=True, message="Robotsim Parameters updated successfully.")

    except Exception as e:
        rospy.logerr("Failed to update parameters: %s", str(e))
        return SetParamResponse(success=False, message="Failed to update robotsim parameters.")

# Main function to initialize the ROS service node
if __name__ == "__main__":
    rospy.init_node("parameter_update_service")

    # Initialize the service with the new parameters
    service = rospy.Service("set_param", SetParam, handle_set_param)

    rospy.loginfo("Parameter update service is ready to set parameters.")
    rospy.spin()
