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
        # if robot.beacon_button_sensor.is_top_red_button_pressed():
        #     ev3.Sound.beep()
        # elif robot.beacon_button_sensor.is_top_blue_button_pressed():
        #     ev3.Sound.speak('Hello. How are you?')



main()