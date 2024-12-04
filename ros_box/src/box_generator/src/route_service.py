#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
from dynamic_reconfigure.client import Client
from box_generator.srv import WaypointSender, WaypointSenderResponse

# Define the list of goals with position and orientation
goals = [
    {
        'position': {'x': 16.67, 'y': 2.76, 'z': 0.0},
        'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': -0.7} #BASE
    },
    {
        'position': {'x': 7.2, 'y': 2.79, 'z': 0.0},
        'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.99} #STOP1
    },
    {
        'position': {'x': 7.2, 'y': 6.69, 'z': 0.0},
        'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': -0.7} #STOP2
    },
    {
        'position': {'x': 1.444, 'y': 2.547, 'z': 0.0},
        'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.99} #STOP3
    },
    {
        'position': {'x': 16.67, 'y': 2.76, 'z': 0.0},
        'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': -0.7} #BACK TO BASE
    }
]

class WP_Sender():

    def __init__(self):
        
        rospy.loginfo("Router init!")
        # Client to move_base service
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    # Function to send a goal to the move_base action server
    def send_goal(self, req):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        goal.target_pose.pose.position.x = req.position_x
        goal.target_pose.pose.position.y = req.position_y
        goal.target_pose.pose.position.z = req.position_z
        
        goal.target_pose.pose.orientation.x = req.orientation_x
        goal.target_pose.pose.orientation.y = req.orientation_y
        goal.target_pose.pose.orientation.z = req.orientation_z
        goal.target_pose.pose.orientation.w = req.orientation_w
        
        rospy.loginfo("Sending goal: position=({}, {}, {}), orientation=({}, {}, {}, {})".format(
            req.position_x, req.position_y, req.position_z,
            req.orientation_x, req.orientation_y, req.orientation_z, req.orientation_w
        ))
        
        try:
            self.client.send_goal(goal)
            self.client.wait_for_result()
            
            # Return True if the goal was reached
            if self.client.get_state() == GoalStatus.SUCCEEDED:
                rospy.loginfo("Goal succeeded!")
                return WaypointSenderResponse(True, f"Done!")
            else:
                rospy.logwarn("Goal failed or was aborted.")
                return WaypointSenderResponse(False, f"Goal failed or was aborted.")
        
        except rospy.ServiceException as e:
            rospy.logerr(f"Service call failed: {e}")
            return WaypointSenderResponse(False, str(e))
        

# Main function
if __name__ == "__main__":
    rospy.init_node('router')
    
    # Create object that contain serve:
    wp_sender = WP_Sender()

    # Crear los servidores de servicios
    router_srv = rospy.Service('router', WaypointSender, wp_sender.send_goal)

    
    rospy.loginfo("Ready to send waypoints")
    rospy.spin()


