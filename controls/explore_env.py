#!/usr/bin/env python2

import time
import threading
from sonar import *
from pibot import PiBot

"""
class used to navigate the env. avoiding any collisions using the
sonar sensor.
"""

MIN_DIS = 20    # minimal distance in centimeters
TURN_TIME = 0.5 # time to turn until checking sonar

def check_distance():
	"""
	Check the distance and return true if dis > 20 cm.
	"""
	dis = read_sensor()
	if dis > MIN_DIS:
		return True
	else:
		return False

class Explore(object):
	def __init__(self):
		"""
		Constructor, sets up the motor and sonar daemons 
		"""
		self.motor_daemon = PiBot()
		self.sonar_daemon = threading.Thread(target=check_distance)
		self.sonar_daemon.daemon = True
	
	def get_stats(self):
		"""
		Returns current pibot stats.
		"""
		return self.motor_daemon.status

	def run(self):
		"""
		Runs the exploration algorithm. Go farward until distance
		check_distance returns false if so turn 40 degrees to the right
		and repeat.
		"""
		while True:
			dis = self.sonar_daemon.start()
			if dis:
				self.motor_daemon.forward()
			else:
				self.motor_daemon.right()
				time.sleep(TURN_TIME)
				self.motor_daemon.forward()