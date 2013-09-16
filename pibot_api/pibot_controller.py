#!/usr/bin/env python2

import json
import RPi.GPIO as gpio

def load_settings():
    """Loads the settings to know gpio ports and returns a dictionary"""
    settings_file = open('gpio_settings.cfg')
    settings = json.load(settings_file)
    
    return settings

def power_on():
    sett = load_settings()
    """Sets up the gpio pins"""
    # set-up pi to use pin numbers
    gpio.setmode(gpio.BOARD)
    # set-up gpio pins
    gpio.setup(sett["PWMA"], gpio.OUT) # Set PWMA
    gpio.setup(sett["AIN2"], gpio.OUT) # Set AIN2
    gpio.setup(sett["AIN1"], gpio.OUT) # Set AIN1
    gpio.setup(sett["STBY"], gpio.OUT) # Set STBY
    gpio.setup(sett["BIN1"], gpio.OUT) # Set BIN1
    gpio.setup(sett["BIN2"], gpio.OUT) # Set BIN2
    gpio.setup(sett["PWMB"], gpio.OUT) # Set PWMB

def fname():
    """docstring for fname"""
    pass
