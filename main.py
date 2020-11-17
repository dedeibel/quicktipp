#!env python3
import argparse

from quicktipp import Quicktipp
from histogram import Histogram, Histogram2d
from journal import write_to_journal, find_in_journal

def test_distribution(n, ignore_blacklist, two_dee):
    q = Quicktipp()
    q.set_ignore_blacklist(ignore_blacklist)
    q.prepare(n)
    if two_dee:
        from histogram import Histogram2d
        histogram = Histogram2d()
    else:
        from histogram import Histogram
        histogram = Histogram()
    histogram.tipps(q.get())
    histogram.skipped(q.get_skipped())
    histogram.show()

def show_distribution(quicktipp, two_dee):
    if two_dee:
        from histogram import Histogram2d
        histogram = Histogram2d()
    else:
        from histogram import Histogram
        histogram = Histogram()
    histogram.tipps(q.get())
    histogram.skipped(q.get_skipped())
    histogram.show()

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Generate good(TM) lotto numbers.')
    parser.add_argument('numbers', metavar='NUMBERS', type=str, nargs=1,
                       help='The amount of numbers you want')
    parser.add_argument('-d', '--dist', dest='show_distribution', action='store_true',
                       help='Additionally shows the number distribution of the generated tips')
    parser.add_argument('-f', '--find', dest='find_numbers', action='store_true',
                       help='Search for the given numbers in the journal four or more matches, comma separated, no spaces as NUMBERS parameter')
    parser.add_argument('-j', '--no-journal', dest='no_journal', action='store_true',
            help='Does not write to journal ~/.quicktipp.log in this run (also does not in -t or -d)')
    parser.add_argument('-p', '--no-prefix', dest='no_prefix', action='store_true',
            help='Prevent showing an index before each tip')
    parser.add_argument('-t', '--test', dest='test_distribution', action='store_true',
                       help='Tests the distribution of n generated and filtered results, use e.g. 10000')
    parser.add_argument('-2', '--two-dee', dest='two_dee', action='store_true', # ;-)
            help='Print distribution histogramm as 2D map of the number coordinates')
    parser.add_argument('-b', '--no-blacklist', dest='no_blacklist', action='store_true',
            help='Ignores the blacklist, kind of useless except for testing')
    parser.add_argument('-v', '--verbose', type=int, default='1',
                       help='Chattyness 0 to 3')
    
    args = parser.parse_args()
    numbers = args.numbers[0]

    if args.find_numbers:
        find_in_journal(numbers)
        exit(0)

    numbers = int(numbers)

    if args.test_distribution:
        test_distribution(numbers, args.no_blacklist, args.two_dee)
        exit(0)

    q = Quicktipp()
    q.set_ignore_blacklist(args.no_blacklist)
    q.set_verbose(args.verbose)
    q.set_print_index_numbers(not args.no_prefix)
    q.prepare(numbers)
    print(str(q))

    if args.show_distribution:
        show_distribution(q, args.two_dee)
    elif not args.no_journal:
        write_to_journal(q)
