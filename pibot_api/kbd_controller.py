#!/usr/bin/env python2

import os
import sys    
import termios
import fcntl

from pibot import *

pibot = PiBot()
control_keys = {'a' : pibot.left,
                's' : pibot.reverse,
                'd' : pibot.right,
                'q' : pibot.slight_left,
                'w' : pibot.forward,
                'e' : pibot.slight_right,
                'f' : pibot.stop}    

def readKeys():
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
            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

readKeys()
