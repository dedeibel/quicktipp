
from helper import find_start, relocate, sorted_coords, coords_le, coords_add, coords_sub, coords_max, coords_move, coords_positive

# Visual pattern on the "lotto board". First coord should be on x = 0. Number of
# coords can be one to six.
# name: Name of the pattern (to see why it was discarded)
# coords: One up to six coords [[x, y], ...] of the pattern, values zero to six
# misses: Amount of coords that don't have to match pattern before testing.
# L, R - Rotate. F - Flip. M - Mirror: ["R", "F"]
class Pattern:
    def __init__(self, name, coords, misses = 0):
        self.name = name
        if not coords:
            raise ValueError('Pattern needs coords')

        self.coords = sorted_coords(coords)
        self.misses = misses

        # pattern bounds min are by definition at 0,0
        # so just look at the last coords for sizes
        # width in coords, so 4 means 3....
        self.width = max([c[0] for c in self.coords])
        self.height = self.coords[-1][1]
    
    def get_name(self):
        return self.name

    # sorted
    def get_coords(self):
        return self.coords

    def get_misses(self):
        return self.misses

    def matches(self, tipp):
        # a lot of methods from helper.py were inlined because of dramatic
        # performance improvements (x2)
        tipp_coords = tipp.get_coords_set()
        inner_coords_max = coords_max(tipp_coords)

        # debug:
        #print("w %d h %d - inner max %s" % (self.width, self.height, str(inner_coords_max)))

        for tipp_coord in tipp_coords:
            for pattern_anchor in self.coords:
                # debug:
                #print("for tipp: %s pattern: %s" % (tipp_coord, pattern_anchor))
                relative = [tipp_coord[0] - pattern_anchor[0], tipp_coord[1] - pattern_anchor[1]]

                # debug:
                #print("rw: %d rh: %d" % (inner_coords_max[0] - relative[0], inner_coords_max[1] - relative[1]))
                if self.misses == 0 and ((inner_coords_max[0] - relative[0]) < self.width or (inner_coords_max[1] - relative[1]) < self.height):
                    continue

                # debug:
                #for ci in self.coords:
                #    print("  %s -- %s in %s?" % (str(relative), [ci[0] + relative[0], ci[1] + relative[1]], tipp_coords))
                match_count = sum(tuple(c) in tipp_coords for c in ([ci[0] + relative[0], ci[1] + relative[1]] for ci in self.coords))

                #print("%s %d of %d: %s" % (self.name, match_count, len(self.coords) - self.misses, (match_count >= len(self.coords) - self.misses)))
                if match_count >= len(self.coords) - self.misses:
                    return True
        return False

    def __str__(self):
        return self.str_pretty(1)

    def __eq__(self, other): 
        if not isinstance(other, Pattern):
            # don't attempt to compare against unrelated types
            return NotImplemented

        # Note: name is not compared!
        # Lazy man's deep equals using str... *sigh* we only have number
        # contents
        return len(self.coords) == len(other.coords) and str(self.coords) == str(other.coords) and self.misses == other.misses


    def __hash__(self):
        # Note: name is not compared!
        # wow, using str here again since python lists seem not that useful
        # here (no deep hashing capabilities by default)
        return hash((str(self.coords), self.misses))

    def str_pretty(self, verbosity = 1):
        s = ''

        if verbosity > 0:
            if self.name:
                s += "name: %s" % self.name
            if self.misses:
                s += " misses: %d" % self.misses

            if verbosity == 1:
                s += "\n" + str(self.coords)
            if verbosity > 1:
                s += "\n" + self._print_sorted_coords(self.coords) + "\n"
        return s

    def _print_sorted_coords(self, csorted):
        max_x = 0
        max_y = 0
        for c in csorted:
            max_x = max(max_x, c[0])
            max_y = max(max_y, c[1])

        s = ''
        c = [0,0]
        for y in range(max_y + 1):
            c[1] = y
            for x in range(max_x + 1):
                c[0] = x
                if c in csorted:
                    s += "x"
                    csorted = csorted[1:]
                else:
                    s += "."
            s += "\n"
        return s

