import unittest
from helper import *

class TestTipp(unittest.TestCase):
    def testfind_start(self):
        self.assertEqual(find_start([[0,0]]), [0,0])
        self.assertEqual(find_start([[2,2]]), [2,2])
        self.assertEqual(find_start([[6,6]]), [6,6])

        self.assertEqual(find_start([[5,5],[3,2],[2,1]]), [2,1])
        self.assertEqual(find_start([[6,6],[6,0]]), [6,0])
        self.assertEqual(find_start([[6,0],[5,6]]), [5,6])

    def test_relocate(self):
        self.assertEqual(relocate(
            [[2,1],[3,1],[3,2],[5,5]], [2,1]),
            [[0,0],[1,0],[1,1],[3,4]])

    def test_move(self):
        self.assertEqual(coords_move(
            [[0,0],[2,1],[1,1],[1,3]], [2,1]),
            [[2,1],[4,2],[3,2],[3,4]])

    def testfind_start_empty(self):
        self.assertRaises(ValueError, lambda: find_start([0,0]))

    def test_calc_coord_y_eq_0(self):
        self.assertEqual(calc_coord(1), [0,0])
        self.assertEqual(calc_coord(4), [3,0])
        self.assertEqual(calc_coord(7), [6,0])

    def test_calc_coord(self):
        self.assertEqual(calc_coord(8), [0,1])
        self.assertEqual(calc_coord(9), [1,1])
        self.assertEqual(calc_coord(14), [6,1])
        self.assertEqual(calc_coord(15), [0,2])
        self.assertEqual(calc_coord(35), [6,4])
        self.assertEqual(calc_coord(36), [0,5])
        self.assertEqual(calc_coord(43), [0,6])
        self.assertEqual(calc_coord(46), [3,6])
        self.assertEqual(calc_coord(49), [6,6])

    def test_get_exception(self):
        self.assertRaises(ValueError, lambda: calc_coord(0))
        self.assertRaises(ValueError, lambda: calc_coord(50))

    def test_sorted_coords(self):
        self.assertEqual(sorted_coords(
            [[1,0],[0,0],[1,1],[0,1]]),
            [[0,0],[1,0],[0,1],[1,1]])

    def test_lt(self):
        self.assertFalse(coords_lt([0,0],[0,0]))
        self.assertFalse(coords_lt([1,0],[0,0]))
        self.assertFalse(coords_lt([0,1],[0,0]))

        self.assertTrue(coords_lt([0,0],[1,0]))
        self.assertTrue(coords_lt([0,0],[0,1]))
        self.assertTrue(coords_lt([0,0],[1,1]))

    def test_le(self):
        self.assertTrue(coords_le([0,0],[0,0]))
        self.assertFalse(coords_le([1,0],[0,0]))
        self.assertTrue(coords_lt([0,0],[1,1]))

    def test_add(self):
        self.assertEqual(coords_add([0,0],[0,0]), [0,0])
        self.assertEqual(coords_add([1,0],[0,2]), [1,2])
        self.assertEqual(coords_add([-1,5],[2,-3]), [1,2])

    def test_sub(self):
        self.assertEqual(coords_sub([0,0],[0,0]), [0,0])
        self.assertEqual(coords_sub([1,0],[0,2]), [1,-2])
        self.assertEqual(coords_sub([-1,5],[2,-3]), [-3,8])

    def test_coords_min(self):
        self.assertEqual(coords_min([[2,3],[-1,5],[0,0],[2,-3]]), [-1,-3])

    def test_coords_max(self):
        self.assertEqual(coords_max([[2,3],[-1,5],[8,0],[2,-3]]), [8,5])

    def test_coords_positive(self):
        self.assertTrue(coords_positive([0,0]))
        self.assertTrue(coords_positive([1,0]))
        self.assertTrue(coords_positive([0,1]))
        self.assertTrue(coords_positive([12,34]))

        self.assertFalse(coords_positive([-1,0]))
        self.assertFalse(coords_positive([0,-1]))
        self.assertFalse(coords_positive([-12,-34]))

    def test_compare_list(self):
        self.assertEqual(compare_list_recurs([3,2,1], [1,1,1]), 1);
        self.assertEqual(compare_list_recurs([3,2], [1,1,1]), 1);

        self.assertEqual(compare_list_recurs([1,1,1], [2,2,1]), -1);
        self.assertEqual(compare_list_recurs([1,1,1], [2]), -1);
        self.assertEqual(compare_list_recurs([3,2], [3,2]), 0);

        self.assertEqual(compare_list_recurs([3,2,1], [3]), 1);

if __name__ == '__main__':
    unittest.main()
