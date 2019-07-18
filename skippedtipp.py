from helper import indent

# Represents a skipped tipp. It contains the reason an the blacklist item and
# can be used to print an explanation (str_pretty)
class SkippedTipp:
    def __init__(self, tipp, reason, blacklist_item = None):
        self.tipp = tipp
        self.reason = reason
        self.blacklist_item = blacklist_item

    def get_numbers(self):
        return self.tipp.numbers()

    def get_reason(self):
        return self.reason

    def __lt__(self, other):
        return self.tipp < other.tipp

    def __str__(self):
        return self.str_pretty(1)

    def str_pretty(self, verbosity = 1):
        s = ''

        if verbosity > 0:
            s += 'Skipped because ' + self.reason
            if self.blacklist_item:
                if verbosity == 1:
                        s += ' ' + self.blacklist_item.get_name() 
                if verbosity > 1:
                    s += ':\n' + indent(self.blacklist_item.str_pretty(verbosity))

            s += '\nNumbers:\n'+ indent(self.tipp.str_pretty(verbosity))
        return s

