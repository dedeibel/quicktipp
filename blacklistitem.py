from helper import coords_min, relocate, calc_coord
from pattern import Pattern

# An entry in the blacklist. Can be matched against a lotto tipp to device
# if it should be discarded. Defined as a form of visual pattern.
class BlacklistItem:
    # name: Name of the item to see why it was discarded
    # coords: One up to six coords [[x, y], ...] of the pattern, values zero to six
    # misses: Amount of coords that don't have to match  
    # transformations: List of transformations that should be applied to the
    # pattern before testing. L, R - Rotate. F - Flip. M - Mirror: ["R", "F"]
    def __init__(self, name, coords, misses = 0, transformations = []):
        self.name = name
        self.misses = misses

        self.main_pattern = Pattern(name, coords, misses)
        self.patterns = [self.main_pattern]

        self.transformations = transformations
        self._perform_transformations()

    def _perform_transformations(self):
        for r in self.transformations:
            rotated_coords = r.perform(self.get_coords())
            min_coord = coords_min(rotated_coords)
            relocated = relocate(rotated_coords, min_coord)
            self.patterns.append(Pattern(self.name +" "+ r.get_suffix(), relocated, self.misses))

    def get_name(self):
        return self.name

    def get_coords(self):
        return self.main_pattern.get_coords()

    def get_patterns(self):
        return self.patterns

    def get_main_pattern(self):
        return self.patterns[0]

    def get_misses(self):
        return self.misses

    def matches(self, tipp):
        for p in self.patterns:
            if p.matches(tipp):
                return True
        return False

    def __str__(self):
        return self.str_pretty(1)

    def str_pretty(self, verbosity = 1):
        s = ''

        if verbosity > 0:
            if verbosity == 1:
                s += self.patterns[0].str_pretty(verbosity)
            if verbosity > 1:
                for p in self.patterns:
                    s += p.str_pretty(verbosity)

        return s

# Blacklist item entry, matches litteraly/directly entered numbers as opposed to patterns.
# Used for example famous numbers.
class BlacklistItemDirect:
    # numbers: [1,2,3,4,5,6]
    def __init__(self, name, numbers, misses = 0):
        self.name = name
        self.misses = misses
        self.numbers = numbers

    def get_name(self):
        return self.name

    def get_coords(self):
        return [calc_coord(int(number)) for number in self.numbers]

    def get_misses(self):
        return self.misses

    def matches(self, tipp):
        matches = 0
        for p in self.numbers:
            if p in tipp.numbers():
                matches += 1
        return matches >= (len(self.numbers) - self.misses)

    def __str__(self):
        return self.str_pretty(1)

    def str_pretty(self, verbosity = 1):
        s = ''

        if verbosity > 0:
            s += ' '.join(['%2d' % e for e in self.numbers])

        return s

# Matches tipps that likely look like a date
class BlacklistItemDate:
    def __init__(self):
        self.name = 'date'

    def get_name(self):
        return self.name

    def get_coords(self):
        return []

    def get_misses(self):
        return 0

    def matches(self, tipp):
        numbers = tipp.numbers()

        if not 19 in numbers and not 20 in numbers:
            return False

        # Recognize date-like numbers
        le31 = sum(num <= 31 for num in numbers)
        # if all numbers except two are less than 31 and two of them less than 13
        if le31 >= 3 and le31 < 6 and any(num <= 12 for num in numbers):
            # Falls dann noch 19xx oder 20xx vor kommt, skipp
            if 19 in numbers:
                return True
            if le31 >= 4: # and 20 in numbers
                return True

    def __str__(self):
        return self.str_pretty(1)

    def str_pretty(self, verbosity = 1):
        s = ''

        if verbosity > 0:
            s += 'date'

        return s
