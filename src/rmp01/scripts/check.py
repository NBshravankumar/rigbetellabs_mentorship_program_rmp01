#!/usr/bin/env python3
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Quaternion, Point
import actionlib

rospy.init_node('send_goal_node')
move_base_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
move_base_client.wait_for_server()
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
x_goal,y_goal=input("enter x,y : ").split(",")
x_goal=float(x_goal)
y_goal=float(y_goal)
goal.target_pose.pose.position = Point(x_goal, y_goal, 0.0)  # x,y here reflected 
goal.target_pose.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)  # not working if removed 1.0
move_base_client.send_goal(goal)
move_base_client.wait_for_result()
rospy.loginfo("Goal Reached")
