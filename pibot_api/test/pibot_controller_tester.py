#!/usr/bin/env python

import sys
sys.path.append("..")
from pibot_controller import *
import time

"""
Script that requires PiBot to be turned on and connected to test.

@author Tim Sizemore
@author Andriy Rudyk
@version 20 September 2013
"""

#Asserts GPIO pins turned on.
print '[!] Turning on GPIO pins.'
power_ctrl(POWER_ON)
print '[+] Turned on GPIO pins.'
time.sleep(2)

#Asserts motor A is moving forward.
print '[!] Starting motor A forward.'
motor_ctrl(MOTOR_A, FORWARD)
print '[+] Started motor A forward.'
time.sleep(2)

#Asserts motor B is moving forward.
print '[!] Starting motor B forward.'
motor_ctrl(MOTOR_B, FORWARD)
print '[+] Started motor B forward.'
time.sleep(2)

#Asserts motor A is moving backward.
print '[!] Starting motor A backward.'
motor_ctrl(MOTOR_A, BACKWARD)
print '[+] Started motor A backward.'
time.sleep(2)

#Assets motor B is moving backward.
print '[!] Starting motor B backward.'
motor_ctrl(MOTOR_B, BACKWARD)
print '[+] Started motor B backward.'
time.sleep(2)

#Asserts motor A stops.
print '[!] Stopping motor A.'
motor_ctrl(MOTOR_A, STOP)
print '[+] Stopped motor A.'
time.sleep(2)

#Asserts motor B stops.
print '[!] Stopping motor B.'
motor_ctrl(MOTOR_B, STOP)
print '[+] Stopped motor B.'
time.sleep(2)

#Asserts motor A is moving forward.
print '[!] Starting motor A forward.'
motor_ctrl(MOTOR_A, FORWARD)
print '[+] Started motor A forward.'
time.sleep(2)

#Asserts motor B is moving forward.
print '[!] Starting motor B forward.'
motor_ctrl(MOTOR_B, FORWARD)
print '[+] Started motor B forward.'
time.sleep(2)

#Asserts motor A is moving backward.
print '[!] Starting motor A backward.'
motor_ctrl(MOTOR_A, BACKWARD)
print '[+] Started motor A backward.'
time.sleep(2)

#Asserts motor B is moving backward.
print '[!] Starting motor B backward.'
motor_ctrl(MOTOR_B, BACKWARD)
print '[+] Started motor B backward.'
time.sleep(2)

#Asserts motor A is moving forward.
print '[!] Starting motor A forward.'
motor_ctrl(MOTOR_A, FORWARD)
print '[+] Started motor A forward.'
time.sleep(2)

#Asserts motor B is moving forward.
print '[!] Starting motor B forward.'
motor_ctrl(MOTOR_B, FORWARD)
print '[+] Started motor B forward.'
time.sleep(2)

#Asserts motor A is stopped.
print '[!] Stopping motor A.'
motor_ctrl(MOTOR_A, STOP)
print '[+] Stopped motor A.'
time.sleep(2)

#Asserts motor B is stopped.
print '[!] Stopping motor B.'
motor_ctrl(MOTOR_B, STOP)
print '[+] Stopped motor B.'
time.sleep(2)

#Asserts GPIO pins are turned off.
print '[!] Turning off GPIO pins.'
power_ctrl(POWER_OFF)
print '[+] Turned off GPIO pins.'
