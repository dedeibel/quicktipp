
import unittest

from tipp import Tipp
from helper import find_start, relocate
from blacklistparser import BlacklistParser

class TestPattern(unittest.TestCase):

    def test_dimension(self):
        bl_item = BlacklistParser.parse("""
        x.x.x
        .x...
        ....x
        """)
        pattern = bl_item.get_main_pattern()
        #self.assertEqual(pattern.width, 5)
        #self.assertEqual(pattern.height, 3)
        # unexpected but it was better to calc with 0 based "width"
        self.assertEqual(pattern.width, 4)
        self.assertEqual(pattern.height, 2)

    def test_matches_simple(self):
        self.line = BlacklistParser.parse('xxxx')
        self.assertTrue(self.line.matches(Tipp([1, 2, 3, 4])))

    def test_misses_big(self):
        blacklist_item = BlacklistParser.parse("""
        misses 2
          .....x
          ....x
          ...x
          ..x
          .x
          x
        """)

        self.assertTrue(blacklist_item.matches(Tipp([43, 37, 31, 25, 19, 13])))
        self.assertTrue(blacklist_item.matches(Tipp([43, 37, 19, 13, 7, 31])))
        self.assertTrue(blacklist_item.matches(Tipp([37, 31, 25, 19, 4, 2])))
        self.assertTrue(blacklist_item.matches(Tipp([44, 38, 32, 26, 4, 2])))
        self.assertTrue(blacklist_item.matches(Tipp([14, 20, 26, 32, 48, 3])))

    def test_match_small(self):
        blacklist_item = BlacklistParser.parse("""
        misses 1
          xx
          xx
        """)

        self.assertTrue(blacklist_item.matches(Tipp([1, 23, 24, 30, 31, 34, 43])))
        self.assertTrue(blacklist_item.matches(Tipp([6, 7, 13, 14, 9, 37, 49])))
        self.assertTrue(blacklist_item.matches(Tipp([41, 42, 48, 49, 9, 37, 2])))
        self.assertTrue(blacklist_item.matches(Tipp([41, 42, 48, 49, 9, 37, 2])))

    def test_match_out_of_bounds(self):
        blacklist_item = BlacklistParser.parse("""
        misses 2
        transform M
          ...x
          xxxx
        """)

        self.assertTrue(blacklist_item.matches(Tipp([1, 16, 24, 38, 40, 41, 42])))

if __name__ == '__main__':
    unittest.main()
