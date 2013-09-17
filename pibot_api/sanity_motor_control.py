#!/usr/bin/python

import time
import RPi.GPIO as GPIO

#Declare the GPIO settings
#print "Set GPIO Board numbers"
# to use Raspberry pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) #Connected to PWMA
GPIO.setup(11, GPIO.OUT) #Connected to AIN2
GPIO.setup(12, GPIO.OUT) #Connected to AIN1
GPIO.setup(13, GPIO.OUT) #Connected to STBY
GPIO.setup(15, GPIO.OUT) #Connected to BIN1
GPIO.setup(16, GPIO.OUT) #Connected to BIN2
GPIO.setup(18, GPIO.OUT) #Connected to PWMB

#Specify the direct to turn the motor
#Clockwise AIN1/BIN1 = HIGH and AIN2/BIN2 = LOW
#Counter-Clockwise: AIN1/BIN1 = LOW and AIN2/BIN2 = HIGH

#First we will drive everything clockwise
#Set the direction of Motor A
GPIO.output(12, GPIO.HIGH) #Set AIN1
GPIO.output(11, GPIO.LOW) #Set AIN2
#Set the Speed / PWM for A
GPIO.output(7, GPIO.HIGH) #Set PWMA

#Set the direction of Motor B
GPIO.output(15, GPIO.HIGH) #Set BIN1
GPIO.output(16, GPIO.LOW) #Set BIN2
#Set the Speed / PWM for B
GPIO.output(18, GPIO.HIGH) #Set PWMA

#Make sure STBY is disabled - Set it to HIGH
GPIO.output(13, GPIO.HIGH)

time.sleep(5)

#Now drive the motor in the other direction (Counter Clockwise)
#Set the direction of Motor A
GPIO.output(12, GPIO.LOW) #Set AIN1
GPIO.output(11, GPIO.HIGH) #Set AIN2
#Set the Speed / PWM for A
GPIO.output(7, GPIO.HIGH) #Set PWMA

#Set the direction of Motor B
GPIO.output(15, GPIO.LOW) #Set BIN1
GPIO.output(16, GPIO.HIGH) #Set BIN2
#Set the Speed / PWM for B
GPIO.output(18, GPIO.HIGH) #Set PWMA

#Make sure STBY is disabled - Set it to HIGH
GPIO.output(13, GPIO.HIGH)

time.sleep(5)

#Now set everything to low (Switch everything Off)
GPIO.output(12, GPIO.LOW) #Set AIN1
GPIO.output(11, GPIO.LOW) #Set AIN2
GPIO.output(7, GPIO.LOW) #Set PWMA
GPIO.output(15, GPIO.LOW) #Set BIN1
GPIO.output(16, GPIO.LOW) #Set BIN2
GPIO.output(18, GPIO.LOW) #Set PWMA
GPIO.output(13, GPIO.LOW) #Set STBY
