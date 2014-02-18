#!/usr/bin/env python2

"""
file: pi_server.py
authors: Andriy Rudyk
         Tim Sizemore
version: 17th December, 2013

PiBot command server.
"""

import argparse # Module for easy argument parsing
import asyncore # Module for asynchronous socket service clients and servers
import socket   # Module with all socket classes/methods
import sys      # Module for retring calling things from the system
import logging  # Module for logging conversations

from pibot import *

HOST_NAME    = 'localhost'  # Default host name
DEFAULT_PORT = 1337         # Default port to listen on
DEFAULT_BUFF = 1024         # Default buffer size
MAX_QUEUE    = 5            # Max. number of hosts queued for listen()

class WelcomeServerSocket(asyncore.dispatcher):
    """ Welcome socket class - handles incoming connections.

    Extends: asyncore.dispatcher - a thin wrapper around a low-level
                                   socket object.
    """
    def __init__(self, port=DEFAULT_PORT):
        """ Constructor - initiates a new dispatcher object for the welcoming
                          socket.  
        Keyword Arguments:
        port -- port number to listen to connections on. (Default 1337)
        """
        asyncore.dispatcher.__init__(self)  # Eqivalent to super in java
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM) # New socket
        self.bind((HOST_NAME, port))
        self.listen(MAX_QUEUE)              # Bind & listen

    def handle_accept(self):
        """ Connection handler - listens and handles all incoming connections.

        Keyword Arguments:
        None
        """
        serverSock, addr = self.accept()    # accept connections
        print 'Connected from: ', addr
        PrivateServerSocket(serverSock)     # Starts the thread

    def handle_error(self):
        """ Handles all socket or thread exceptions or errors.

        Only gets called when exception can not be handled.
        
        Keyword Arguments:
        None
        """
        print 'An unexpected error has occured, exiting...'
        sys.exit(1)

class PrivateServerSocket(asyncore.dispatcher_with_send):
    """ Threading class, handles each connection

    Extends: asyncore.dispatcher_with_send - a thin wrapper around a low-level
                                             socket object, with sending
                                             capability.
    """
    def handle_read(self):
        """ Connection handler - listens and handles input from each client.
                             thsi is threaded.
        Keyword Arguments:
        None
        """
        pibot = PiBot()
        dataRecvd = self.recv(DEFAULT_BUFF)
        if dataRecvd:                           # If connection lives, continue
            print "[*] command -> " + dataRecvd.lower()
            cmd = dataRecvd.lower().strip()
            # New HTPP
            if 'GET' in cmd:
                print 'retriving information'
                if cmd.split(' ')[1] == 'forward':
                    pibot.forward()
                if cmd.split(' ')[1] == 'reverse':
                    pibot.reverse()
                if cmd.split(' ')[1] == 'left':
                    pibot.left()
                if cmd.split(' ')[1] == 'right':
                    pibot.right()
            if 'DO' in cmd:
                print 'listening to commands'
                self.send(pibot.get_sonar())

        else: 
            self.close()                      # Connection is dead, close
            pibot.stop()

    def handle_close(self):
        """ Close handler - closes the connection & cleans up the maps.

        Keyword Agruments:
        None
        """
        print 'Disconnected from: ', self.getpeername()

    def handle_error(self):
        """ Handles all socket or thread exceptions or errors.

        Only gets called when exception can not be handled.
        
        Keyword Arguments:
        None
        """
        print 'An unexpected error has occured, exiting...'
        sys.exit(1)


if __name__ == '__main__':
    """ Main method, the entry into the program.

        All exception handling for network is done by asyncore.
    """
    argParser = argparse.ArgumentParser(        # Create argument parser
        prog='./pi_server.py',
        description='A Python implementation of a PiBot command server',
        epilog='Developers: Andriy Rudyk | Tim Sizemore'
    )

    argParser.add_argument('port', metavar='PORT', type=int,
        help='port number for server to listen on')
    argParser.add_argument('-l', '--log', type=str, default='serverlog.log',
        help='log used for logging conversations')

    args = argParser.parse_args()               # Parse arguments
                                                # Create logs (below)
    logging.basicConfig(filename=args.log, level=logging.INFO)
    try:                                        # Run, handle keyboard interrupt
        print 'Server online'                   # ctrl-c -> legit exit
        WelcomeServerSocket(args.port)
        asyncore.loop()
    except KeyboardInterrupt:
        print 'Server killed'
