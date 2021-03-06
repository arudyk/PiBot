import json
import RPi.GPIO as gpio

"""
Another script based class that contains the lowest level of abraction between
PiBot and its controls.

@author Tim Sizemore
@author Andriy Rudyk
@version 20 September 2013
"""

#Global varibles that correspond with engine controls.
POWER_ON =  1
POWER_OFF = 0

#Global varibles that correspond with distinct engines.
MOTOR_A  = 'a'
MOTOR_B  = 'b'

#Global varibles that correspond with PiBot's direction.
FORWARD  =  1
STOP     =  0
BACKWARD = -1

def load_settings():
    """Loads the settings to know gpio ports and returns a dictionary"""
    settings_file = open('/home/pi/PiBot/pibot_api/gpio_settings.cfg')
    settings = json.load(settings_file)
    
    return settings

#Configures the settings from the gpio_settings.cfg file.
sett = load_settings()

def power_ctrl(circuit):
    """Determines what engine needs to be turned and and executes it."""
    if circuit == POWER_ON:
        gpio.setmode(gpio.BOARD)
        gpio.setup(sett["PWMA"], gpio.OUT) 
        gpio.setup(sett["AIN2"], gpio.OUT) 
        gpio.setup(sett["AIN1"], gpio.OUT) 
        gpio.setup(sett["STBY"], gpio.OUT) 
        gpio.setup(sett["BIN1"], gpio.OUT) 
        gpio.setup(sett["BIN2"], gpio.OUT) 
        gpio.setup(sett["PWMB"], gpio.OUT) 
    elif circuit == POWER_OFF:
        gpio.output(sett["AIN1"], gpio.LOW)
        gpio.output(sett["AIN2"], gpio.LOW)
        gpio.output(sett["PWMA"], gpio.LOW)
        gpio.output(sett["BIN1"], gpio.LOW)
        gpio.output(sett["BIN2"], gpio.LOW)
        gpio.output(sett["PWMB"], gpio.LOW)
        gpio.output(sett["STBY"], gpio.LOW)

def motor_ctrl(motor, dir):
    """Controls motors for PiBot"""
    gpio.output(sett["STBY"], gpio.HIGH)

    if motor == MOTOR_A:
        if dir == FORWARD:
            gpio.output(sett["AIN1"], gpio.HIGH) # Set AIN1 \ direction of motor A
            gpio.output(sett["AIN2"], gpio.LOW)  # Set AIN2 / 
            gpio.output(sett["PWMA"], gpio.HIGH)  # Set AIN2 / 
        elif dir == BACKWARD:
            gpio.output(sett["AIN1"], gpio.LOW) # Set AIN1 \ direction of motor A
            gpio.output(sett["AIN2"], gpio.HIGH)  # Set AIN2 / 
            gpio.output(sett["PWMA"], gpio.HIGH)  # Set AIN2 / 
        elif dir == STOP:
            gpio.output(sett["AIN1"], gpio.LOW)
            gpio.output(sett["AIN2"], gpio.LOW)
            gpio.output(sett["PWMA"], gpio.LOW)  # Set AIN2 / 
    elif motor == MOTOR_B: 
        if dir == FORWARD:
            gpio.output(sett["BIN1"], gpio.HIGH) # Set AIN1 \ direction of motor A
            gpio.output(sett["BIN2"], gpio.LOW)  # Set AIN2 / 
            gpio.output(sett["PWMB"], gpio.HIGH)  # Set AIN2 / 
        elif dir == BACKWARD:
            gpio.output(sett["BIN1"], gpio.LOW) # Set AIN1 \ direction of motor A
            gpio.output(sett["BIN2"], gpio.HIGH)  # Set AIN2 / 
            gpio.output(sett["PWMB"], gpio.HIGH)  # Set AIN2 / 
        elif dir == STOP:
            gpio.output(sett["BIN1"], gpio.LOW)
            gpio.output(sett["BIN2"], gpio.LOW)
            gpio.output(sett["PWMB"], gpio.LOW)  # Set AIN2 / 
