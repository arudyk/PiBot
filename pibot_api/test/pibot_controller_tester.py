#!/usr/bin/env python2

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

print '[!] Starting motor A forward.'
motor_ctrl(MOTOR_A, FORWARD)
print '[+] Started motor A forward.'
time.sleep(2)
