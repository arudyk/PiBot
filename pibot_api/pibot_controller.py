import json
import RPi.GPIO as gpio

FORWARD  =  1
BACKWARD = -1

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

def power_off():
    """Turns off the gpio pins"""
    gpio.output(sett["AIN1"], gpio.LOW)
    gpio.output(sett["AIN2"], gpio.LOW)
    gpio.output(sett["PWMA"], gpio.LOW)
    gpio.output(sett["BIN1"], gpio.LOW)
    gpio.output(sett["BIN2"], gpio.LOW)
    gpio.output(sett["PWMA"], gpio.LOW)
    gpio.output(sett["STBY"], gpio.LOW)

def motor_a(dir):
    """Controls motor A"""
    gpio.output(sett["STBY"], gpio.HIGH)

    if dir == FORWARD:
        gpio.output(sett["AIN1"], gpio.HIGH) # Set AIN1 \ direction of motor A
        gpio.output(sett["AIN2"], gpio.LOW)  # Set AIN2 / 
    elif dir == BACKWARD:
        gpio.output(sett["AIN1"], gpio.LOW) # Set AIN1 \ direction of motor A
        gpio.output(sett["AIN2"], gpio.HIGH)  # Set AIN2 / 
        
    gpio.output(sett["PWMA"], gpio.HIGH)

def motor_b(dir):
    """Controls motor B"""
    gpio.output(sett["STBY"], gpio.HIGH)

    if dir == FORWARD:
        gpio.output(sett["BIN1"], gpio.HIGH) # Set AIN1 \ direction of motor A
        gpio.output(sett["BIN2"], gpio.LOW)  # Set AIN2 / 
    elif dir == BACKWARD:
        gpio.output(sett["BIN1"], gpio.LOW) # Set AIN1 \ direction of motor A
        gpio.output(sett["BIN2"], gpio.HIGH)  # Set AIN2 / 
        
    gpio.output(sett["PWMB"], gpio.HIGH)
