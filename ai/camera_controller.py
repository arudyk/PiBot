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
import io
import cv2

def take_picture(filename, width, height):
    """
    Takes a picture width x height and saves us filename.
    """
    picamera.resolution = (width, height)
    # According to API camera needs 0.2 seconds warm up at start.
    time.sleep(0.2)
    camera.capture(filename)

def ocv_object():
    """
    Takes a picture then converts that data to an array that Open CV can use.
    """
    stream = io.BytesIO()
    with picamera.PiCamera() as cam
        cam.start_preview()
        time.sleep(2)
        camera.capture(stream, format='jpeg')

    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data, 1)
    image = image[:, :, ::-1]

def remove_picture(filename):
    """
    Removes filename
    """
    os.remove(filename)
