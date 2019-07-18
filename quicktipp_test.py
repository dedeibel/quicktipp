import unittest

from quicktipp import Quicktipp

class TestQuicktipp(unittest.TestCase):
    def test_smoke(self):
        q = Quicktipp()

        q.prepare(20)
        self.assertEqual(len(q.get()), 20)

        self.assertEqual(type(q.get_skipped()), list)

        q.prepare(0)
        self.assertEqual(len(q.get()), 0)

        q.prepare(5)
        self.assertEqual(len(q.get()), 5)

        q.set_ignore_blacklist(True)
        q.set_verbose(3)
        q.prepare(5)
        self.assertEqual(len(q.get()), 5)

if __name__ == '__main__':
    unittest.main()
