from tipp import Tipp
from helper import neunundvierzig, sattolo
from blacklist import Blacklist

# Genrates "ifinite" tipps which are filtered using the playlist using an iterator
# style way by calling "next".
#
# Skipped tipps are collected in a list, call get_skipped to get them.
class TippGenerator:
    bl = Blacklist()

    def __init__(self):
        self.current_pool = neunundvierzig()
        self.skipped = []
        self.ignore_blacklist = False

    def reset(self):
        self.skipped.clear()
        self.next()

    def _get_tipp(self):
        return Tipp(list(self.current_pool[:6]))

    def set_ignore_blacklist(self, ignore):
        self.ignore_blacklist = ignore

    def next(self):
        tipp = None
        skipp = None
        while True:
            sattolo(self.current_pool)
            tipp = self._get_tipp()

            if self.ignore_blacklist:
                return tipp

            skipp = self.bl.contains(tipp)
            if skipp:
                self.skipped.append(skipp)
            else:
                return tipp

    def get_skipped(self):
        return self.skipped

    def __str__(self):
        return "current: [%s] skipped [%s]" % (self.current_pool, self.skipped)

