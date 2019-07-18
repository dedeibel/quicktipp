import unittest

from datetime import datetime

from journal import write_to_journal_str, find_in_journal_str
from quicktipp import Quicktipp
from tipp import Tipp
from skippedtipp import SkippedTipp

class TestJournal(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2019, 7, 18, 21, 8, 0, 0)

    def test_write(self):
        q = Quicktipp()
        q.tipps = [
                Tipp([1,2,3,4,5,6]),
                Tipp([7,14,21,28,35,42])
        ]
        q.skipped = [
            SkippedTipp(Tipp([2,3,4,5,6,7]), 'mock1'),
            SkippedTipp(Tipp([8,15,22,29,36,43]), 'mock2')
        ]

        self.assertEqual(write_to_journal_str(q, self.now), """
2019-07-18T21:08:00: skipped  2  3  4  5  6  7 mock1
2019-07-18T21:08:00: skipped  8 15 22 29 36 43 mock2
2019-07-18T21:08:00: tipp     1  2  3  4  5  6
2019-07-18T21:08:00: tipp     7 14 21 28 35 42
""".lstrip())

    def test_find(self):
        journal = """
2019-07-18T21:08:00: skipped  2  3  4  5  6  7 mock1
2019-07-18T21:08:00: skipped  8 15 22 29 36 43 mock2
2019-07-18T21:08:00: tipp     1  2  3  4  5  6
2019-07-18T21:08:00: tipp     7 14 21 28 35 42
""".lstrip()

        lines = journal.split("\n")
        self.assertTrue(find_in_journal_str(lines[0], ['1', '2', '3', '4', '5', '6']))
        self.assertTrue(find_in_journal_str(lines[1], ['8', '15', '22', '29', '36', '43']))
        self.assertTrue(find_in_journal_str(lines[2], ['2', '3', '4', '5', '6', '7']))

        self.assertTrue(find_in_journal_str(lines[1], ['8', '15', '22', '29', '36', '44']))  # 5 of 6
        self.assertTrue(find_in_journal_str(lines[1], ['8', '15', '22', '29', '37', '44']))  # 4 of 6
        self.assertFalse(find_in_journal_str(lines[1], ['8', '15', '22', '28', '37', '44'])) # 3 of 6

        self.assertFalse(find_in_journal_str(lines[1], ['8', '4', '2', '8', '3', '42'])) # 0 of 6

        self.assertEqual(find_in_journal_str(lines[1], ['8', '15', '22', '29', '36', '44']),
                '2019-07-18T21:08:00: skipped  8 15 22 29 36 43 mock2 (5 matches)')  # 5 of 6

if __name__ == '__main__':
    unittest.main()
