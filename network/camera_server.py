#!/usr/bin/env python2

import io
from socket import socket
import struct
from PIL import Image

class CameraServer(self):
	def __init__(self, ip_address, port):
		self.server_socket = socket()
		server_socket.bind((ip_address, port))
		server_socket.listen(0)

	def listen(self):
		connection = self.server_socket.accept()[0].makefile('rb')
		try:
			while True:
				# Read the length of the image as 32 bit unsigned int.
				# If length is zero quit the loop.
				image_len = struct.unpack('<L', connection.read(4))[0]
				if not image_len:
					break
				# Make stream
				image_stream = io.BytesIO()
				image_stream.write(connection.read(image_len))
				# Open it 
				image_stream.seek(0)
				image = Image.open(image_stream)
				# print image.size
				image.verify()
		finally:
			connection.close()
			server_socket.close()