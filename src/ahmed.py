"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    def tests():
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

    def test_go_straight_inches():
        robot.drive_system.go_straight_inches(6)

    def test_wait_until_intensity_is_less_than():
        robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
        robot.color_sensor.wait_until_intensity_is_less_than(25)
        robot.drive_system.stop_moving()

    def test_wait_until_intensity_is_greater_than():
        robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
        robot.color_sensor.wait_until_intensity_is_greater_than(75)
        robot.drive_system.stop_moving()

    def test_wait_until_color_is():
        robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
        robot.color_sensor.wait_until_color_is(3)
        robot.drive_system.stop_moving()

    def test_wait_until_color_is_one_of():
        robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
        robot.color_sensor.wait_until_color_is_one_of([2, 3, 4, 5])
        robot.drive_system.stop_moving()

    def test_wait_until_pressed():
        robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
        robot.touch_sensor.wait_until_pressed()
        robot.drive_system.stop_moving()

    def test_wait_until_released():
        robot.touch_sensor.wait_until_pressed()
        robot.drive_system.start_moving(left_wheel_duty_cycle_percent=25, right_wheel_duty_cycle_percent=25)
        robot.touch_sensor.wait_until_released()
        robot.drive_system.stop_moving()

    robot = rb.Snatch3rRobot()
    tests()



main()
