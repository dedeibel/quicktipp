import unittest

from tipp import Tipp
from helper import find_start, relocate
from blacklistparser import BlacklistParser

class TestBlacklistItem(unittest.TestCase):
    def test_matches(self):
        self.line = BlacklistParser.parse('xxxx')

        self.assertTrue(self.line.matches(Tipp([1, 2, 3, 4])))
        self.assertTrue(self.line.matches(Tipp([3, 4, 5, 6])))

        self.assertTrue(self.line.matches(Tipp([43, 44, 45, 46])))
        self.assertTrue(self.line.matches(Tipp([46, 47, 48, 49])))

        self.assertTrue(self.line.matches(Tipp([2, 3, 4, 5, 6, 7])))

        self.assertFalse(self.line.matches(Tipp([2, 3, 4, 12, 6, 7])))

    def test_matches_complex(self):
        pattern = BlacklistParser.parse("""
        xx...xx
        x.....x
        ...x...
        x.....x
        xx...xx
        """)

        self.assertTrue(pattern.matches(Tipp([
            1, 2, 6, 7,
            8, 14,
            18,
            22, 28,
            29, 30, 34, 35])))

        self.assertFalse(pattern.matches(Tipp([
            1, 2, 6, 7,
            8, 14,
            22, 28,
            29, 30, 34, 35])))

        self.assertTrue(pattern.matches(Tipp([
            8, 9, 13, 14,
            15, 21,
            25,
            29, 35,
            36, 37, 41, 42])))

    def test_matches_partial(self):
        pattern = BlacklistParser.parse("""
        misses 2
        xx...xx
        x.....x
        """)

        self.assertTrue(pattern.matches(Tipp([
            1, 2, 6, 7])))
        self.assertFalse(pattern.matches(Tipp([
            1, 2, 6])))

        # note: 2 instead of 1 would not match!
        self.assertTrue(pattern.matches(Tipp([
            1, 6, 8, 14])))

        pattern = BlacklistParser.parse("""
        misses 2
        xxxxxx
        """)

        self.assertTrue(pattern.matches(Tipp([
            1, 2, 3, 4, 5, 6])))
        self.assertTrue(pattern.matches(Tipp([
            2, 3, 4, 5, 6])))
        self.assertTrue(pattern.matches(Tipp([
            2, 3, 4, 5])))
        self.assertTrue(pattern.matches(Tipp([
            1, 2, 5, 6])))

        self.assertFalse(pattern.matches(Tipp([
            1, 2, 3])))

    def test_match_with_misses_big(self):
        blacklist_item = BlacklistParser.parse("""
        misses 2
        transform R
          x..
          .x
          ..x
          ...x
          ....x
          .....x
        """)

        self.assertTrue(blacklist_item.matches(Tipp([9, 17, 25, 33, 41, 3, 12])))
        self.assertTrue(blacklist_item.matches(Tipp([43, 37, 19, 13, 7, 1, 31])))

if __name__ == '__main__':
    unittest.main()
