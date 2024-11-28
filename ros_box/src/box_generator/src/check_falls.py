#!/usr/bin/env python

import rospy
from gazebo_msgs.msg import ModelStates, LinkStates
from std_srvs.srv import Empty
from std_msgs.msg import Bool

# Standard threshold values for x and y directions in meters
THRESHOLDS_XY = [0.8, 0.6]
# Base z threshold
BASE_Z_THRESHOLD = 0.3


# Dictionary to track logged warnings for each box
logged_warnings = {}  # {box_name: True/False}

class FallsChecker():
    def __init__(self):
        rospy.init_node('check_falls')

        rospy.loginfo('Offset tracking started')

        # Subscribe to the Gazebo model states topic
        self.pub =rospy.Publisher('/reset_sim', Bool, queue_size = 10)
        #rospy.Subscriber('/gazebo/model_states', ModelStates, self.gazebo_callback)
        rospy.Subscriber('/gazebo/link_states', LinkStates, self.gazebo_callback)
  
        # Global atributes:
        self.base_pose = [0, 0, 0]

    def run(self):
        rospy.spin()

    def gazebo_callback(self, msg):
        global logged_warnings
        current_time = rospy.get_time()  # Get the current time

        for name, pose in zip(msg.name, msg.pose):
            if name == "mir::base_footprint":
                # Update base pose
                self.base_pose = [pose.position.x, pose.position.y, pose.position.z]

            if name.startswith("Box_"):  # Check all boxes that start with "Box_"
                # Current box pose
                box_pose = [pose.position.x, pose.position.y, pose.position.z]
                self.check_offset(name, box_pose)

    def check_offset(self, box_name, box_pose):
        global logged_warnings
        delta = [abs(self.base_pose[i] - box_pose[i]) for i in range(2)]

        thresholds = THRESHOLDS_XY

        above_threshold = any(d > threshold for d, threshold in zip(delta, thresholds))
        # rospy.loginfo(f"Box pose: {box_pose}")
        # rospy.loginfo(f"MIR pose: {self.base_pose}")
        # Log warning only if not already logged for this box
        if above_threshold and not logged_warnings.get(box_name, False):
            for i, (d, threshold) in enumerate(zip(delta, thresholds)):
                if d > threshold:
                    rospy.logwarn(f"\n{'*' * 30}\nOffset exceeded in {'XYZ'[i]} direction for {box_name}: {d:.2f} > {threshold:.2f}\n{'*' * 30}\n")
                    logged_warnings[box_name] = True  # Mark warning logged for this box
                    
                    logged_warnings = {} # Reset the logged_warnings dictionary
            self.pub.publish(False)
        else:
            self.pub.publish(True)

if __name__ == '__main__':
    try:
        node = FallsChecker()
        node.run()

    except rospy.ROSInterruptException:
        pass

