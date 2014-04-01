#!/usr/bin/env python2

"""
Andriy Rudyk
Tim Sizemore
"""

#
# WORK IN PROGRESS...
#

import numpy as np
import cv2

THRSHLD1 = 1.3
THRSHLD2 = 5

def setup_detection(xml_list, img)
	"""
	Add all xml files ti list (zml files represent objects)
	"""
	img = cv2.imread('faces.jpg', 0) # Get a greyscale image
	
	cascades = []					 # Setup a list of "objects" from xml files 
	for xml in xml_list:
		cascades.append(cv2.CascadeClassifier(xml))

	objects = []
	for cascade in cascades:
		cascade.detectMultiScale(gray, THRSHLD1, THRSHLD2)

	return cascades
