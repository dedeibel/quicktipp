import unittest
from tipp import Tipp

class TestTipp(unittest.TestCase):
    def setUp(self):
        self.tipp = Tipp([1,7,14,36,46,49])

    def test_get_coords(self):
        self.assertEqual(self.tipp.get_coords(),
                [[0,0],[6,0],[6,1],[0,5],[3,6],[6,6]])

    def test_get_coords_set(self):
        self.assertEqual(self.tipp.get_coords_set(),
                {(0,0),(6,0),(6,1),(0,5),(3,6),(6,6)})

if __name__ == '__main__':
    unittest.main()
