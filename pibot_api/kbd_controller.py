#!/usr/bin/env python2

import os
import sys    
import termios
import fcntl

control_keys = {'a' : 'left',
                's' : 'rear',
                'd' : 'right',
                'q' : 'slight_left',
                'w' : 'forward',
                'e' : 'slight_right'}

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
                c = sys.stdin.read(1)
                if c in control_keys.keys():
                    print 'you pressed controlled key ', control_keys[c]
            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

readKeys()
