#!/usr/bin/env python

import sys
sys.path.append("..")
from pibot_controller import *
import time

print '[!] Turning on GPIO pins.'
power_ctrl(POWER_ON)
print '[+] Turned on GPIO pins.'
time.sleep(2)

print '[!] Starting motor A forward.'
motor_ctrl(MOTOR_A, FORWARD)
print '[+] Started motor A forward.'
time.sleep(2)

print '[!] Starting motor B forward.'
motor_ctrl(MOTOR_B, FORWARD)
print '[+] Started motor B forward.'
time.sleep(2)

print '[!] Starting motor A backward.'
motor_ctrl(MOTOR_A, BACKWARD)
print '[+] Started motor A backward.'
time.sleep(2)

print '[!] Starting motor B backward.'
motor_ctrl(MOTOR_B, BACKWARD)
print '[+] Started motor B backward.'
time.sleep(2)

print '[!] Stopping motor A.'
motor_ctrl(MOTOR_A, STOP)
print '[+] Stopped motor A.'
time.sleep(2)

print '[!] Stopping motor B.'
motor_ctrl(MOTOR_B, STOP)
print '[+] Stopped motor B.'
time.sleep(2)

print '[!] Starting motor A forward.'
motor_ctrl(MOTOR_A, FORWARD)
print '[+] Started motor A forward.'
time.sleep(2)

print '[!] Starting motor B forward.'
motor_ctrl(MOTOR_B, FORWARD)
print '[+] Started motor B forward.'
time.sleep(2)

print '[!] Starting motor A backward.'
motor_ctrl(MOTOR_A, BACKWARD)
print '[+] Started motor A backward.'
time.sleep(2)

print '[!] Starting motor B backward.'
motor_ctrl(MOTOR_B, BACKWARD)
print '[+] Started motor B backward.'
time.sleep(2)

print '[!] Starting motor A forward.'
motor_ctrl(MOTOR_A, FORWARD)
print '[+] Started motor A forward.'
time.sleep(2)

print '[!] Starting motor B forward.'
motor_ctrl(MOTOR_B, FORWARD)
print '[+] Started motor B forward.'
time.sleep(2)

print '[!] Stopping motor A.'
motor_ctrl(MOTOR_A, STOP)
print '[+] Stopped motor A.'
time.sleep(2)

print '[!] Stopping motor B.'
motor_ctrl(MOTOR_B, STOP)
print '[+] Stopped motor B.'
time.sleep(2)

print '[!] Turning off GPIO pins.'
power_ctrl(POWER_OFF)
print '[+] Turned off GPIO pins.'
time.sleep(2)
