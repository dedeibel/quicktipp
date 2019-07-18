import unittest

import matplotlib.pyplot as plt

from quicktipp import Quicktipp
from histogram import Histogram, Histogram2d

class TestHistogram(unittest.TestCase):
    def tearDown(self):
        plt.close()

    def test_smoke(self):
        q = Quicktipp()
        q.prepare(20)
        histogram = Histogram()
        histogram.tipps(q.get())
        histogram.skipped(q.get_skipped())

    def test_smoke2d(self):
        q = Quicktipp()
        q.prepare(20)
        histogram = Histogram2d()
        histogram.tipps(q.get())
        histogram.skipped(q.get_skipped())

if __name__ == '__main__':
    unittest.main()
