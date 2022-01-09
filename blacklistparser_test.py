import unittest

from blacklistparser import BlacklistParser
from tipp import Tipp
from pattern import Pattern

class TestBlacklistParser(unittest.TestCase):
    def test_empty(self):
        self.assertRaises(ValueError, lambda: BlacklistParser.parse("").get_coords())

    def test_oneline(self):
        self.assertEqual(BlacklistParser.parse('x').get_coords(), [[0,0]])
        self.assertEqual(BlacklistParser.parse('x.').get_coords(), [[0,0]])
        self.assertEqual(BlacklistParser.parse('xx').get_coords(), [[0,0], [1,0]])
        self.assertEqual(BlacklistParser.parse('x.x').get_coords(), [[0,0], [2,0]])

    def test_2d(self):
        self.assertEqual(BlacklistParser.parse("""
        x..
        .x.
        ..x
        """).get_coords(), [[0,0], [1,1], [2,2]])

        self.assertEqual(BlacklistParser.parse("""
        xx...xx
        x.....x
        ...x...
        x.....x
        xx...xx
        """).get_coords(), [
            [0,0], [1,0],[5,0],[6,0],
            [0,1],             [6,1],
                     [3,2]          ,
            [0,3],             [6,3],
            [0,4], [1,4],[5,4],[6,4]]
        )

    def test_misses(self):
        blacklist_item = BlacklistParser.parse("""
        misses 2
        xx
        .x
        """)
        self.assertEqual(blacklist_item.get_coords(), [[0,0], [1,0], [1,1]])
        self.assertEqual(blacklist_item.get_misses(), 2)

        blacklist_item2 = BlacklistParser.parse("""
        missing 3
        x
        """)
        self.assertEqual(blacklist_item2.get_coords(), [[0,0]])
        self.assertEqual(blacklist_item2.get_misses(), 3)

    def test_name(self):
        blacklist_item = BlacklistParser.parse("""
        name Prince Albert
        misses 1
        x
        """)
        self.assertEqual(blacklist_item.get_name(), "Prince Albert")
        self.assertEqual(blacklist_item.get_coords(), [[0,0]])
        self.assertEqual(blacklist_item.get_misses(), 1)

    def test_rotate_name(self):
        blacklist_item = BlacklistParser.parse("""
        name Rotate Test
        transform L
        misses 1
        xx
        """)

        self.assertEqual(len(blacklist_item.get_patterns()), 2)
        original = blacklist_item.get_patterns()[0]
        rot_r = blacklist_item.get_patterns()[1]
        self.assertEqual(original.get_name(), "Rotate Test")
        self.assertEqual(rot_r.get_name(), "Rotate Test L90")

    def test_rotate_zero_based(self):
        blacklist_item = BlacklistParser.parse("""
        name Rotate Test Zero
        transform L
        misses 1
        x.x.x
        x
        """)

        self.assertEqual(len(blacklist_item.get_patterns()), 8)
        rot_r = blacklist_item.get_patterns()[1]
        self.assertEqual(rot_r.get_coords(), [[0,0],[0,2],[0,4],[1,4]])

    def test_left_then_mirror(self):
        blacklist_item = BlacklistParser.parse("""
        name LM Test
        transform LM
        x
        xxx
        """)

        self.assertEqual(len(blacklist_item.get_patterns()), 8)
        self.assertTrue(Pattern("LM Test L", [[0,0],[0,1],[0,2],[1,2]], 0) in blacklist_item.get_patterns())

    def test_right_then_mirror(self):
        blacklist_item = BlacklistParser.parse("""
        name RM Test
        transform RM
        x
        xxx
        """)

        self.assertEqual(len(blacklist_item.get_patterns()), 8)
        rot_r = blacklist_item.get_patterns()[1]
        self.assertTrue(Pattern("RM Test RM", [[0,0],[1,0],[1,1],[1,2]], 0) in blacklist_item.get_patterns())

    def test_rotate_relocate(self):
        blacklist_item = BlacklistParser.parse("""
        name Rotate Test Relocate
        transform L
        ..
        xx
        """)

        self.assertEqual(len(blacklist_item.get_patterns()), 2)
        original = blacklist_item.get_patterns()[0]
        rot_r = blacklist_item.get_patterns()[1]

        self.assertEqual(original.get_coords(), [[0,0],[1, 0]])
        self.assertEqual(rot_r.get_coords(), [[0,0],[0,1]])

    def test_rotate_multi(self):
        blacklist_item = BlacklistParser.parse("""
        name Rotate Test Multi
        transform L, R, M, F
        xxx
        x
        """)

        self.assertEqual(len(blacklist_item.get_patterns()), 8)
        ori = blacklist_item.get_patterns()[0]
        rot_l = blacklist_item.get_patterns()[1]
        rot_l180 = blacklist_item.get_patterns()[2]
        rot_r = blacklist_item.get_patterns()[3]
        rot_m = blacklist_item.get_patterns()[4]
        rot_ml90 = blacklist_item.get_patterns()[5]
        rot_ml180 = blacklist_item.get_patterns()[6]
        rot_mr90 = blacklist_item.get_patterns()[7]
        self.assertEqual(ori.get_name(), "Rotate Test Multi")
        self.assertEqual(rot_l.get_name(), "Rotate Test Multi L90")
        self.assertEqual(rot_l180.get_name(), "Rotate Test Multi L180")
        self.assertEqual(rot_m.get_name(), "Rotate Test Multi Mirror")
        self.assertEqual(rot_r.get_name(), "Rotate Test Multi R90")
        self.assertEqual(rot_ml90.get_name(), "Rotate Test Multi ML90")
        self.assertEqual(rot_ml180.get_name(), "Rotate Test Multi ML180")
        self.assertEqual(rot_mr90.get_name(), "Rotate Test Multi MR90")

        self.assertEqual(ori.get_coords(), [[0,0],[1, 0],[2,0],[0,1]])
        self.assertEqual(rot_l.get_coords(), [[0,0],[0, 1],[0,2],[1,2]])
        self.assertEqual(rot_r.get_coords(), [[0,0],[1, 0],[1,1],[1,2]])
        self.assertEqual(rot_m.get_coords(),  [[0,0],[1, 0],[2,0],[2,1]])
        self.assertEqual(rot_ml180.get_coords(),  [[0,0],[0,1],[1, 1],[2,1]])

    def test_parse_number(self):
        blacklist_item = BlacklistParser.parse("""
        name numbers1
        misses 1
        numbers 5, 10, 15, 20, 25, 30
        """)

        self.assertEqual(blacklist_item.get_coords(), [[4,0],[2,1],[0,2],[5,2],[3,3],[1,4]])
        self.assertTrue(blacklist_item.matches(Tipp([5, 10, 15, 20, 25, 30])))
        self.assertTrue(blacklist_item.matches(Tipp([4, 10, 15, 20, 25, 30])))
        self.assertFalse(blacklist_item.matches(Tipp([4, 9, 15, 20, 25, 30])))

if __name__ == '__main__':
    unittest.main()
