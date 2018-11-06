"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time

robot = rb.Snatch3rRobot()


def polygon(n):
    for k in range(n):
        robot.DriveSystem.go_straight_inches(6)
        robot.DriveSystem.turn_degrees((n-2)*(180/n))





def arm_and_claw():
    robot.arm.move_arm_to_position(3)

arm_and_claw()