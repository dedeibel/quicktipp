from functools import cmp_to_key

from helper import compare_list_recurs, compare_coords, calc_coord

# A lotto tipp (tip)
# 6 numbers out of 1 to 49.
#
# Numbers and coords are usually stored sorted
class Tipp:
    def __init__(self, numbers, max_num = 49, print_nums_per_line = 7):
        self.num = numbers
        self.max_num = max_num
        self.print_nums_per_line = print_nums_per_line

        self.num.sort()
        self.coords = self._get_coords_sorted()

    def numbers(self):
        return self.num

    # sorted
    def get_coords(self):
        return self.coords

    def get_coords_set(self):
        return frozenset(tuple([tuple(c) for c in self.coords]))

    def _get_coords_sorted(self):
        return sorted(
                [calc_coord(number, self.print_nums_per_line) for number in self.num],
                key=cmp_to_key(compare_coords))

    def __lt__(self, other):
        return compare_list_recurs(self.num, other.num) < 0

    def __str__(self):
        return self.str_pretty(1)

    def str_pretty(self, verbosity = 1):
        s = ''

        if verbosity == 1:
            s += ' '.join(['%2d' % e for e in self.num])
        if verbosity > 1:
            for n in range(1, self.max_num + 1):
                if n in self.num:
                    s += "%2d" % n;
                else:
                    s += " .";
                s += ' '
                if n > 1 and n % self.print_nums_per_line == 0:
                    s += "\n"
        return s

