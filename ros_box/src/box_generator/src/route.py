#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
from dynamic_reconfigure.client import Client


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

# Function to send a goal to the move_base action server
def send_goal(client, goal_position, goal_orientation):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = goal_position['x']
    goal.target_pose.pose.position.y = goal_position['y']
    goal.target_pose.pose.position.z = goal_position['z']
    
    goal.target_pose.pose.orientation.x = goal_orientation['x']
    goal.target_pose.pose.orientation.y = goal_orientation['y']
    goal.target_pose.pose.orientation.z = goal_orientation['z']
    goal.target_pose.pose.orientation.w = goal_orientation['w']
    
    rospy.loginfo("Sending goal: position=({}, {}, {}), orientation=({}, {}, {}, {})".format(
        goal_position['x'], goal_position['y'], goal_position['z'],
        goal_orientation['x'], goal_orientation['y'], goal_orientation['z'], goal_orientation['w']
    ))
    
    client.send_goal(goal)
    client.wait_for_result()

    # Return True if the goal was reached
    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo("Goal succeeded!")
        return True
    else:
        rospy.logwarn("Goal failed or was aborted.")
        return False

# Main function
if __name__ == "__main__":
    rospy.init_node('goal_sequence_node')
    
    
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()
    
    for goal_data in goals:
        position = goal_data['position']
        orientation = goal_data['orientation']
        
        # Send the goal and wait for completion
        if not send_goal(client, position, orientation):
            rospy.logerr("Failed to reach goal. Stopping sequence.")
            break
    
    rospy.loginfo("All goals processed.")



# #!/usr/bin/env python3

# import rospy
# import actionlib
# from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
# from actionlib_msgs.msg import GoalStatus


# def send_goal(client, goal_position, goal_orientation):
#     goal = MoveBaseGoal()
#     goal.target_pose.header.frame_id = "map"
#     goal.target_pose.header.stamp = rospy.Time.now()

#     goal.target_pose.pose.position.x = goal_position['x']
#     goal.target_pose.pose.position.y = goal_position['y']
#     goal.target_pose.pose.position.z = goal_position['z']

#     goal.target_pose.pose.orientation.x = goal_orientation['x']
#     goal.target_pose.pose.orientation.y = goal_orientation['y']
#     goal.target_pose.pose.orientation.z = goal_orientation['z']
#     goal.target_pose.pose.orientation.w = goal_orientation['w']

#     rospy.loginfo("Sending goal: position=({}, {}, {}), orientation=({}, {}, {}, {})".format(
#         goal_position['x'], goal_position['y'], goal_position['z'],
#         goal_orientation['x'], goal_orientation['y'], goal_orientation['z'], goal_orientation['w']
#     ))

#     client.send_goal(goal)
#     client.wait_for_result()

#     # Return True if the goal was reached
#     if client.get_state() == GoalStatus.SUCCEEDED:
#         rospy.loginfo("Goal succeeded!")
#         return True
#     else:
#         rospy.logwarn("Goal failed or was aborted.")
#         return False


# def send_goal_sequence(goal_list):
#     """
#     This function sends a sequence of navigation goals to a robot using ROS.

#     Args:
#         goal_list: List of dictionaries containing goal positions and orientations.
#             Each dictionary should have keys 'position' and 'orientation'.
#             'position' should be a dictionary with keys 'x', 'y', 'z'.
#             'orientation' should be a dictionary with keys 'x', 'y', 'z', 'w'.

#     Returns:
#         None
#     """

#     rospy.init_node('goal_sequence_node')

#     client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
#     client.wait_for_server()

#     for goal_data in goal_list:
#         position = goal_data['position']
#         orientation = goal_data['orientation']

#         # Send the goal and wait for completion
#         if not send_goal(client, position, orientation):
#             rospy.logerr("Failed to reach goal. Stopping sequence.")
#             break

#     rospy.loginfo("All goals processed.")


# if __name__ == "__main__":
#     # Define your goal list (same format as before)
#     goal_list = [
#         {
#             'position': {'x': 16.67, 'y': 2.76, 'z': 0.0},
#             'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': -0.7}  # BASE
#         },
#         {
#             'position': {'x': 7.2, 'y': 2.79, 'z': 0.0},
#             'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.99}  # STOP1
#         },
#         # ... other goals ...
#     ]

#     # Call the send_goal_sequence function with your goal list
#     send_goal_sequence(goal_list)
