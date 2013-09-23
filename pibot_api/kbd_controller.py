#!/usr/bin/env python

import os
import sys    
import termios
import fcntl

from pibot import *

"""
Uses keyboard input to control pibot functions.

@author Tim Sizemore
@author Andriy Rudyk
@version 20 September 2013
"""
#Creates a new PiBot object.
pibot = PiBot()

#A dictionary mapping key presses to PiBot functions.
control_keys = {'a' : pibot.left,
                's' : pibot.reverse,
                'd' : pibot.right,
                'q' : pibot.slight_left,
                'w' : pibot.forward,
                'e' : pibot.slight_right,
                'f' : pibot.stop}    

def print_help():
    """Print a help message"""
    print "+---------+----------------+----------------------------+"
    print "|   Key   |   Action       |   Description              |"
    print "+---------+----------------+----------------------------+"
    print "|   w     |   forward      | Moves PiBot forwards       |"
    print "|   s     |   reverse      | Moves PiBot in reverse     |"
    print "|   a     |   left         | Moves PiBot left           |"
    print "|   d     |   right        | Moves PiBot right          |"
    print "|   q     |   slight-left  | Moves PiBot slightly left  |"
    print "|   e     |   slight-right | Moves PiBot slightly right |"
    print "|   f     |   stop         | Stops PiBot (low voltage)  |"
    print "+---------+----------------+----------------------------+"

def readKeys():
    """Waits for keyboard input and calls the method that is mapped to it."""
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO # dont echo back
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    
    try:        
        while True:            
            try:
                key = sys.stdin.read(1)
                if key in control_keys.keys():
                    control_keys[key]()
                elif key == 'x':
                    pibot.stop()
                    sys.exit(0)
            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

print_help()
readKeys()
