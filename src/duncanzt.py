"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time

def polygon(n):
    robot = rb.Snatch3rRobot()
    for k in range(n):
        robot.DriveSystem.go_straight_inches(6)
        robot.DriveSystem.turn_degrees((n-2)*(180/n))





    






def main():
    """ Runs YOUR specific part of the project """









main()
polygon(6)
