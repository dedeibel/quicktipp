import unittest

from tipp import Tipp
from helper import find_start, relocate
from blacklistparser import BlacklistParser
from blacklistitem import BlacklistItemDirect, BlacklistItemDate

class TestBlacklistItem(unittest.TestCase):
    def setUp(self):
        self.line = BlacklistParser.parse('xxxx')

    def testfind_start(self):
        self.assertEqual(find_start([[0,0]]), [0,0])
        self.assertEqual(find_start([[2,2]]), [2,2])
        self.assertEqual(find_start([[6,6]]), [6,6])

        self.assertEqual(find_start([[5,5],[3,2],[2,1]]), [2,1])
        self.assertEqual(find_start([[6,6],[6,0]]), [6,0])
        self.assertEqual(find_start([[6,0],[5,6]]), [5,6])

    def testfind_start_empty(self):
        self.assertRaises(ValueError, lambda: find_start([0,0]))

    def test_matches(self):
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

class TestBlacklistItemDirect(unittest.TestCase):
    def test_regular(self):
        item = BlacklistItemDirect("d1", [2,3,5,7,9,12], 0)
        self.assertEqual(item.get_name(), "d1")
        self.assertEqual(item.get_misses(), 0)
        self.assertTrue(item.matches(Tipp([2,3,5,7,9,12])))
        self.assertFalse(item.matches(Tipp([2,3,5,7,9,1])))

    def test_missing1(self):
        item = BlacklistItemDirect("d2", [1,11,22,33,44,49], 2)
        self.assertEqual(item.get_name(), "d2")
        self.assertEqual(item.get_misses(), 2)
        self.assertTrue(item.matches(Tipp([9,10,22,33,44,49])))
        self.assertFalse(item.matches(Tipp([9,10,13,33,44,49])))

class TestBlacklistItemDate(unittest.TestCase):
    def test_regular(self):
        item = BlacklistItemDate()
        self.assertTrue(item.matches(Tipp([1,2,19,40,44,39,38])))
        self.assertTrue(item.matches(Tipp([3,6,19,40,45,48,49])))
        self.assertTrue(item.matches(Tipp([3,10,19,40,20,30,49])))

        self.assertFalse(item.matches(Tipp([1,2,20,40,44,39,38])))
        self.assertTrue(item.matches(Tipp([1,2,20,30,44,39,38])))

        self.assertFalse(item.matches(Tipp([1,2,10,40,44,39,38])))
        self.assertFalse(item.matches(Tipp([1,2,3,4,5,19])))
        self.assertFalse(item.matches(Tipp([30,32,33,44,39,38])))

if __name__ == '__main__':
    unittest.main()
