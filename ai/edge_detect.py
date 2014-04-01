#!/usr/bin/env python2

"""
Andriy Rudyk
Tim Sizemore

Finds edges in an image using the "Canny86" algorithm
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt # For testing only

THRSHLD1 = 100
THRSHLD2 = 200

def load_image(image):
	"""
	Loads image into opwncv object.
	"""
	img = cv2.imread(image, 0) # zero for grey scale
	return img

def find_edges(image):
	"""
	Finds image edges according to 
	"""
	edges = cv2.Canny(image, THRSHLD1, THRSHLD2) # image, threshold1, threshold2
	return edges

# TESTER ONLY
if __name__ == "__main__":
	img = load_image('test_pic.jpg')
	edges = find_edges(img)

	plt.subplot(121),plt.imshow(img,cmap = 'gray') # Use grey image (easier for processing)
	plt.title('Original Image'), plt.xticks([]), plt.yticks([]) # Load initial image into plot
	
	plt.subplot(122),plt.imshow(edges,cmap = 'gray')
	plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

	# Display both to screen
	plt.show()
