#!/usr/bin/env python2

import socket, ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_sock = ssl.wrap_socket(s)
ssl_sock.connect(('127.0.0.1', 1337))

print "Connected to", repr(ssl_sock.getpeername())

ssl_sock.write("Duck")

#recvd = ssl_sock.recv(1024)
#print recvd

ssl_sock.close()
