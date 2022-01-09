import numpy as np

# Tested in BlacklistParser_test
class MMult:
    def get_suffix(self):
        return self.suffix

    def perform(self, coords):
        return [(np.array(c) * self.r).getA1().tolist() for c in coords]

class L90(MMult):
    def __init__(self):
        self.suffix = 'L90'
        self.r = np.matrix([[0, -1],[1, 0]])

class L180(MMult):
    def __init__(self):
        self.suffix = 'L180'
        self.r = np.matrix([[0, -1],[1, 0]]) * np.matrix([[0, -1],[1, 0]])

class R90(MMult):
    def __init__(self):
        self.suffix = 'R90'
        self.r = np.matrix([[0, 1],[-1, 0]])

class R180(MMult):
    def __init__(self):
        self.suffix = 'R180'
        self.r = np.matrix([[0, 1],[-1, 0]]) * np.matrix([[0, 1],[-1, 0]])

class Mirror(MMult):
    def __init__(self):
        self.suffix = 'Mirror'
        self.r = np.matrix([[-1, 0],[0, 1]])

class ML90(MMult):
    def __init__(self):
        self.suffix = 'ML90'
        self.r = np.matrix([[-1, 0],[0, 1]]) * np.matrix([[0, -1],[1, 0]])

class ML180(MMult):
    def __init__(self):
        self.suffix = 'ML180'
        self.r = np.matrix([[-1, 0],[0, 1]]) * np.matrix([[0, -1],[1, 0]]) * np.matrix([[0, -1],[1, 0]])

class MR90(MMult):
    def __init__(self):
        self.suffix = 'MR90'
        self.r = np.matrix([[-1, 0],[0, 1]]) * np.matrix([[0, 1],[-1, 0]])

class MR180(MMult):
    def __init__(self):
        self.suffix = 'MR180'
        self.r = np.matrix([[-1, 0],[0, 1]]) * np.matrix([[0, 1],[-1, 0]]) * np.matrix([[0, 1],[-1, 0]])


# Rotation examples
#
# ------
# Pattern:
# xx..
# ..xx
#
# - L
# .x
# .x
# x.
# x.
# 
# - R (same)
# .x
# .x
# x.
# x.
# 
# - M
# ..xx
# xx..
# 
# - F (Mirror, then rot 180)
# 1 M
# ..xx
# xx..
# 
# 2 R90
# x.
# x.
# .x
# .x
# 
# 3 R90
# ..xx
# xx..
# 
# - LM (Rotate 90 left then mirror)
# x.
# x.
# .x
# .x
# 
# - RM (Rotate 90 right then mirror) (same)
# x.
# x.
# .x
# .x
#
#
# ----------
#
# Shape:
# x..
# xxx
# 
# - L
# .x
# .x
# xx
# 
# - R
# xx
# x.
# x.
# 
# - M
# ..x
# xxx
# 
# - F
# 1 M
# ..x
# xxx
# 
# 1 R90
# x
# x
# xx
# 
# 2 R90
# xxx
# x
# 
# - LM
# x
# x
# xx
# 
# - RF
# xx
# .x
# .x
