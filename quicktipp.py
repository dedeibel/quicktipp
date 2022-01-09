from tippgenerator649 import TippGenerator649
from tippgenerator550 import TippGenerator550
 
# Provide lotto tipps (tip) for 6 of 49, german lottery
class Quicktipp:
    def __init__(self, tipp_generator = TippGenerator649()):
        self.generator = tipp_generator
        self.tipps = []
        self.skipped = []
        self.verbose = 1
        self.print_index_numbers = False

    # Configure verbosity of "str"
    # 0 - no output
    # 1 - efficient output
    # 2 - output with ascii art
    def set_verbose(self, verbose):
        self.verbose = verbose

    def set_print_index_numbers(self, print_index_numbers):
        self.print_index_numbers = print_index_numbers

    # Do not test tipps for backlist entries
    def set_ignore_blacklist(self, ignore):
        self.generator.set_ignore_blacklist(ignore)

    def _reset(self):
        self.tipps.clear()
        self.generator.reset()

    # Shuffle and draw numbers
    def prepare(self, anzahl):
        self._reset()

        for i in range(0, anzahl):
            self.tipps.append(self.generator.next())

        if self.generator.get_skipped():
            self.skipped.extend(self.generator.get_skipped())
        self.tipps.sort()
        self.skipped.sort()

    # Get a list of skipped numbers with explanation
    def get_skipped(self):
        return self.skipped

    # Get the prepared tipps
    def get(self):
        return self.tipps

    def __str__(self):
        s = ''

        if self.verbose > 0:
            if self.verbose > 1:
                s += "Skipped (%d)\n" % len(self.skipped)
                if self.verbose > 1:
                    for skipped in self.skipped:
                        s += skipped.str_pretty(self.verbose) + "\n"

                s += "Tipps (%d)\n" % len(self.tipps)
            nr = 1
            for tipp in self.tipps:
                if nr > 1:
                    s += "\n"
                if self.verbose > 1:
                    s += "#%d\n" % nr
                elif self.print_index_numbers:
                    s += "%3d: " % nr
                nr += 1
                s += tipp.str_pretty(self.verbose)
        return s

