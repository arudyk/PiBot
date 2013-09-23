from pibot_controller import *
"""
A class that represents the PiBot controls in their abstracted form.

@author Tim Sizemore
@author Andriy Rudyk
@version 20 September 2013
"""

class PiBot(object):
    """Class representing PiBot"""
    def __init__(self):
        """The PiBot constructor."""
        self.status = None
        power_ctrl(POWER_ON)

    def forward(self):
        """Moves PiBot forward"""
        motor_ctrl(MOTOR_A, FORWARD)
        motor_ctrl(MOTOR_B,FORWARD)
        self.status = "forward"
    
    def reverse(self):
        """Moves PiBot backward"""
        motor_ctrl(MOTOR_A, BACKWARD)
        motor_ctrl(MOTOR_B, BACKWARD)
        self.status = "reverse"

    def left(self):
        """Moves PiBot left on a zero turn radius"""
        motor_ctrl(MOTOR_A, BACKWARD)
        motor_ctrl(MOTOR_B, FORWARD)
        self.status = "zeroleft"

    def right(self):
        """Moves PiBot right on a zero turn radius"""
        motor_ctrl(MOTOR_A, FORWARD)
        motor_ctrl(MOTOR_B, BACKWARD)
        self.status = "zeroright"

    def slight_left(self):
        """Moves PiBot gradually to the left"""
        motor_ctrl(MOTOR_B, FORWARD)
        motor_ctrl(MOTOR_A, STOP)
        self.status = "slightleft"

    def slight_right(self):
        """Moves PiBot gradually to the right"""
        motor_ctrl(MOTOR_A, FORWARD)
        motor_ctrl(MOTOR_B, STOP)
        self.status = "slightright"

    def stop(self):
        """Stops the PiBot"""
        power_ctrl(POWER_OFF)
        self.status = "stop"
