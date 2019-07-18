import numpy as np

# Tested in BlacklistParser_test
class MMult:
    def get_suffix(self):
        return self.suffix

    def perform(self, coords):
        return [(np.array(c) * self.r).getA1().tolist() for c in coords]

class RotateLeft(MMult):
    def __init__(self):
        self.suffix = 'L'
        self.r = np.matrix([[0, -1],[1, 0]])

class RotateRight(MMult):
    def __init__(self):
        self.suffix = 'R'
        self.r = np.matrix([[0, 1],[-1, 0]])

class Mirror(MMult):
    def __init__(self):
        self.suffix = 'M'
        self.r = np.matrix([[-1, 0],[0, 1]])

class Flip(MMult):
    def __init__(self):
        self.suffix = 'F'
        # mirror and rotate 180
        self.r = np.matrix([[-1, 0],[0, 1]]) * np.matrix([[0, 1],[-1, 0]]) * np.matrix([[0, 1],[-1, 0]])

