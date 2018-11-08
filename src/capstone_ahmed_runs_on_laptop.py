"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Tom Ahmed.
"""
# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
from tkinter import *
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    # setup_drive_gui(root, mqtt_client)
    setup_speak_gui(root, mqtt_client)

    root.mainloop()
    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------


def setup_drive_gui(root_window, mqtt):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    speed_entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, mqtt)


def setup_speak_gui(root_window, mqtt):
    frame = ttk.Frame(root_window, padding=20)
    frame.grid()

    variable = StringVar(frame)
    variable.set('line1')

    line_list = ['line1', 'line2', 'line3']
    lines_menu = ttk.OptionMenu(frame, variable, line_list[0], *line_list)
    lines_menu.grid()

    go_button = ttk.Button(frame, text='Start')
    go_button.grid()

    go_button['command'] = \
        lambda: handle_start(variable, mqtt)


def handle_start(var, mqtt):
    line_to_robot = var.get()

    mqtt.send_message('speak', line_to_robot)


def handle_go_forward(entry_box, mqtt):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed_str = entry_box.get()

    mqtt.send_message('go_forward',
                      [speed_str])

    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------


main()
