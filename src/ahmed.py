"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3


def tests(robot):
    test_go_straight_inches()
    time.sleep(2)
    test_wait_until_intensity_is_less_than()
    time.sleep(2)
    test_wait_until_intensity_is_greater_than()
    time.sleep(2)
    test_wait_until_color_is()
    time.sleep(2)
    test_wait_until_color_is_one_of()
    time.sleep(2)
    test_wait_until_pressed()
    time.sleep(2)
    test_wait_until_released()
    robot.drive_system.stop_moving()


def test_go_straight_inches(robot):
    robot.drive_system.go_straight_inches(6)


def test_wait_until_intensity_is_less_than(robot):
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.color_sensor.wait_until_intensity_is_less_than(25)
    robot.drive_system.stop_moving()


def test_wait_until_intensity_is_greater_than(robot):
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.color_sensor.wait_until_intensity_is_greater_than(75)
    robot.drive_system.stop_moving()


def test_wait_until_color_is(robot, color):
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.color_sensor.wait_until_color_is(color)
    robot.drive_system.stop_moving()


def test_wait_until_color_is_one_of(robot):
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.color_sensor.wait_until_color_is_one_of([2, 3, 4, 5])
    robot.drive_system.stop_moving()


def test_wait_until_pressed(robot):
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.touch_sensor.wait_until_pressed()
    robot.drive_system.stop_moving()


def test_wait_until_released(robot):
    robot.touch_sensor.wait_until_pressed()
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.touch_sensor.wait_until_released()
    robot.drive_system.stop_moving()


def follow_line(robot):
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=50, right_wheel_duty_cycle_percent=50)
    while True:
        robot.color_sensor.wait_until_intensity_is_greater_than(75)
        robot.drive_system.stop_moving()
        robot.drive_system.left_wheel.start_spinning(duty_cycle_percent=75)
        robot.color_sensor.wait_until_intensity_is_less_than(25)
        robot.drive_system.left_wheel.stop_spinning()
        robot.drive_system.start_moving(left_wheel_duty_cycle_percent=50, right_wheel_duty_cycle_percent=50)


def find_blob(robot):
    while True:
        blob1 = robot.camera.get_biggest_blob()
        print(blob1.get_area())
        # if blob1.get_area() >= 600:
        #     ev3.Sound.beep().wait()
        #     break


def main():
    """ Runs YOUR specific part of the project """

    robot = rb.Snatch3rRobot()
    # tests(robot)
    follow_line(robot)
    find_blob(robot)


main()
