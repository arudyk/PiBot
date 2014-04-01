#!/usr/bin/env python2

"""
Andriy Rudyk
Tim Sizemore

Camera operation module

###TODO: Look into networking using picamera
"""

import picamera
from time import sleep
import os

def take_picture(filename, width, height):
	"""
	Takes a picture width x height and saves us filename.
	"""
	picamera.resolution = (width, height)
	# According to API camera needs 0.2 seconds warm up at start.
	time.sleep(0.2)
	camera.capture(filename)

def remove_picture(filename):
	"""
	Removes filename
	"""
	os.remove(filename)