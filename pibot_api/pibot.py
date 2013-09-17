from pibot_controller import *

class PiBot(object):
    """Class representing PiBot"""
    def __init__(self):
        self.status = None
        power_on()

    def forward(self):
        """Moves PiBot forward"""
        motor_a(FORWARD)
        motor_b(FORWARD)
        self.status = "forward"
    
    def backward(self):
        """Moves PiBot backward"""
        motor_a(BACKWARD)
        motor_b(BACKWARD)
        self.status = "backward"

    def left(self):
        """Moves PiBot left on a zero turn radius"""
        motor_a(BACKWARD)
        motor_b(FORWARD)
        self.status = "zeroleft"

    def right(self):
        """Moves PiBot right on a zero turn radius"""
        motor_a(FORWARD)
        motor_b(BACKWARD)
        self.status = "zeroright"

    def slight_left(self):
        """Moves PiBot gradually to the left"""
        motor_b(FORWARD)
        self.status = "slightleft"

    def slight_right(self):
        """Moves PiBot gradually to the right"""
        motor_a(FORWARD)
        self.status = "slightright"

    def stop(self):
        """Stops the PiBot"""
        power_off()
