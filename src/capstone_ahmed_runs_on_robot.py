"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Tom Ahmed.
"""
# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        :type robot: rb.Snatch3rRobot
        :param robot:
        """
        self.robot = robot

    def speak(self, line_to_robot):
        ev3.Sound.speak(line_to_robot).wait()

    def pickup(self):
        """
        :type robot: rb.Snatch3rRobot
        :param robot:
        """
        self.robot.drive_system.right_wheel.start_spinning(50)
        self.robot.drive_system.left_wheel.start_spinning(-50)
        while True:
            print(self.robot.camera.get_biggest_blob())
            if self.robot.camera.get_biggest_blob().get_area() >= 500:
                time.sleep(.45)
                self.robot.drive_system.stop_moving()
                break
        distance = self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
        print(self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches())
        self.robot.drive_system.go_straight_inches(distance, 50)

    def go_forward(self, speed):
        speed = int(speed)
        self.robot.drive_system.start_moving(speed, speed)


def main():
    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        #
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work


main()
