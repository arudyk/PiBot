#!/usr/bin/env python

import sys
sys.path.append("..")
from pibot import *
import time

"""
Script that requires PiBot to be on and connected to test the API functionality.

@author Tim Sizemore
@author Andriy Rudyk
@version 20 September 2013
"""

#Creates a new PiBot object.
pibot = PiBot()

#test forward()
print '[!] Attempting to move forward.'
pibot.forward()
if pibot.status == 'forward': print '[+] Moving forward.'
time.sleep(2)

#test reverse()
print '[!] Attempting to move backward.'
pibot.reverse()
if pibot.status == 'reverse': print '[+] Moving backward.'
time.sleep(2)

#test left()
print '[!] Attempting to move zero left.'
pibot.left()
if pibot.status == 'zeroleft': print '[+] Moving zero left.'
time.sleep(2)

#test right()
print '[!] Attempting to move zero right.'
pibot.right()
if pibot.status == 'zeroright': print '[+] Moving zero right.'
time.sleep(2)

#test slight_left()
print '[!] Attempting to move slight left.'
pibot.slight_left()
if pibot.status == 'slightleft': print '[+] Moving slight left.'
time.sleep(2)

#test slight_right()
print '[!] Attempting to move slight right.'
pibot.slight_right()
if pibot.status == 'slightright': print '[+] Moving slight right.'
time.sleep(2)

#test stop()
print '[!] Attempting to stop.'
pibot.stop()
if pibot.status == 'stop': print '[+] Stopped.'
