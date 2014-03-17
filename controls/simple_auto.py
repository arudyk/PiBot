#!/usr/bin/env python2

import time
import RPi.GPIO as GPIO
from pibot import *

DANGER = 5;

def another_right_turn():
    pibot = PiBot();
    if pibot.read_senor() <= DANGER:
        pibot.right()


