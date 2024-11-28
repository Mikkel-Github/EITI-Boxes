#!/bin/bash
cd ~/catkin_ws/EITI-Boxes-main/ros_box/

# Source the ROS setup file for your workspace
source ~/catkin_ws/EITI-Boxes-main/ros_box/devel/setup.bash

# Run the param_service.py node
rosrun box_generator param_service.py

