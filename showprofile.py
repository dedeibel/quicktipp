#!env python3
import pstats
import sys
from pstats import SortKey

# show profiles recorded with "kernprof"

p = pstats.Stats(sys.argv[1])
#p.sort_stats(SortKey.CUMULATIVE).print_stats(40)
p.sort_stats('tottime').print_stats(40)
#stats.sort_stats("percall")
#stats.sort_stats("tottime")
#stats.print_stats(30)
