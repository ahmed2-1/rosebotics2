"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3


def tests(robot):
    test_go_straight_inches(robot)
    time.sleep(15)
    test_wait_until_intensity_is_less_than(robot)
    time.sleep(2)
    test_wait_until_intensity_is_greater_than(robot)
    # time.sleep(2)
    # test_wait_until_color_is(robot)
    # time.sleep(2)
    # test_wait_until_color_is_one_of(robot)
    time.sleep(2)
    test_wait_until_pressed(robot)
    time.sleep(2)
    test_wait_until_released(robot)
    robot.drive_system.stop_moving()


def test_go_straight_inches(robot):
    print("Testing go_straight_inches().")
    robot.drive_system.go_straight_inches(6)


def test_wait_until_intensity_is_less_than(robot):
    print('Testing wait_until_intensity_is_less_than().')
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.color_sensor.wait_until_intensity_is_less_than(25)
    robot.drive_system.stop_moving()


def test_wait_until_intensity_is_greater_than(robot):
    print('Testing wait_until_intensity_is_greater_than().')
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.color_sensor.wait_until_intensity_is_greater_than(75)
    robot.drive_system.stop_moving()


def test_wait_until_color_is(robot, color):
    print('Testing wait_until_color_is().')
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.color_sensor.wait_until_color_is(color)
    robot.drive_system.stop_moving()


def test_wait_until_color_is_one_of(robot):
    print('Testing wait_until_color_is_one_of().')
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.color_sensor.wait_until_color_is_one_of([2, 3, 4, 5])
    robot.drive_system.stop_moving()


def test_wait_until_pressed(robot):
    print('Testing wait_until_pressed().')
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.touch_sensor.wait_until_pressed()
    robot.drive_system.stop_moving()


def test_wait_until_released(robot):
    print('Testing wait_until_released(). Please press touch sensor.')
    robot.touch_sensor.wait_until_pressed()
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
    robot.touch_sensor.wait_until_released()
    robot.drive_system.stop_moving()


def follow_line(robot):
    print('Testing follow_line().')
    robot.drive_system.start_moving(left_wheel_duty_cycle_percent=50, right_wheel_duty_cycle_percent=50)
    while True:
        robot.color_sensor.wait_until_intensity_is_greater_than(75)
        robot.drive_system.stop_moving()
        robot.drive_system.left_wheel.start_spinning(duty_cycle_percent=75)
        robot.color_sensor.wait_until_intensity_is_less_than(25)
        robot.drive_system.left_wheel.stop_spinning()
        robot.drive_system.start_moving(left_wheel_duty_cycle_percent=50, right_wheel_duty_cycle_percent=50)


def find_blob(robot):
    print('Testing find_blob().')
    while True:
        blob1 = robot.camera.get_biggest_blob()
        if blob1.get_area() >= 1500:
            ev3.Sound.beep().wait()


def main():

    """ Runs YOUR specific part of the project """

    robot = rb.Snatch3rRobot()
    # tests(robot)
    # time.sleep(2)
    # follow_line(robot)
    # time.sleep(10)
    # robot.drive_system.stop_moving()
    # time.sleep(2)
    find_blob(robot)


main()
