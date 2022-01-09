
import unittest

from blacklist import Blacklist
from tipp import Tipp

class TestPatterns(unittest.TestCase):
    def test_line(self):
        bl = Blacklist()

        self.assertTrue(bl.contains(Tipp([1, 2, 3, 4, 5])))
        self.assertTrue(bl.contains(Tipp([1, 2, 3, 4])))
        self.assertTrue(bl.contains(Tipp([1,    3, 4, 5])))
        self.assertTrue(bl.contains(Tipp([37, 38, 39])))

    def test_roto(self):
        bl = Blacklist()

        self.assertTrue(bl.contains(Tipp([29, 37, 45])))
        self.assertTrue(bl.contains(Tipp([31, 37, 43])))
        self.assertTrue(bl.contains(Tipp([30, 38, 46])))

    def test_diagonal(self):
        bl = Blacklist()

        self.assertTrue(bl.contains(Tipp([1, 9, 17, 25, 33, 41])))
        self.assertTrue(bl.contains(Tipp([9, 17, 25, 33, 41, 49])))
        
        self.assertTrue(bl.contains(Tipp([1, 9, 17, 33, 41, 3])))
        self.assertTrue(bl.contains(Tipp([9, 17, 25, 33, 41, 5])))

        self.assertTrue(bl.contains(Tipp([29, 23, 17, 11, 5, 9])))

    def test_little_cup(self):
        bl = Blacklist()

        self.assertTrue(bl.contains(Tipp([17, 24, 26, 32, 37, 48])))

    def test_corners(self):
        bl = Blacklist()

        self.assertTrue(bl.contains(Tipp([1, 7, 43, 49, 24, 33])))

    def test_fuenfer_abstand(self):
        bl = Blacklist()

        self.assertTrue(bl.contains(Tipp([5, 10, 15, 20, 25, 30])))

    def test_zc(self):
        bl = Blacklist()

        self.assertTrue(bl.contains(Tipp([8,   9, 17, 18])))
        self.assertTrue(bl.contains(Tipp([10, 11, 15, 16])))

        self.assertTrue(bl.contains(Tipp([10, 17, 23, 30])))
        self.assertTrue(bl.contains(Tipp([ 9, 16, 24, 31])))

if __name__ == '__main__':
    unittest.main()
