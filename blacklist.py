from patterns import PATTERNS
from skippedtipp import SkippedTipp
from blacklistparser import BlacklistParser
from blacklistitem import BlacklistItemDate

# List of tipp patterns and numbers to ignore
class Blacklist:
    def __init__(self):
        self.patterns = [BlacklistParser.parse(ps) for ps in PATTERNS]
        self.patterns.append(BlacklistItemDate())
        # debugging: use only a specific pattern
        #self.patterns = [p for p in self.patterns if p.name == "corners"]

    # If the tipp matches a blacklist entry a "SkippedTipp" explaining the
    # reason is returned - None otherwise.
    def contains(self, tipp):

        for bl_item in self.patterns:
            if bl_item.matches(tipp):
                return SkippedTipp(tipp, 'blacklist pattern', bl_item)

        return None
