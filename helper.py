import re

from functools import cmp_to_key
from random import randrange
from constants import MAX_COORD

# relocates to start
# can produce negative coords, but is okay since we'll rotate
# blacklist patterns and there we get the same result
def relocate(coordinates, start_coord):
    ret = []
    for c in coordinates:
        ret.append(coords_sub(c, start_coord))
    return ret

def coords_move(coords, t):
    return [[c[0] + t[0], c[1] + t[1]] for c in coords]

def find_start(coordinates):
    c = [0,0]
    for x in range(7):
      c[0] = x
      for y in range(7):
        c[1] = y
        if c in coordinates:
            return c
    raise ValueError("no numbers in tipp")

# bounding box min
def coords_min(coords):
    m = [MAX_COORD, MAX_COORD]
    for c in coords:
        m[0] = min(m[0], c[0])
        m[1] = min(m[1], c[1])
    return m

# bounding box max
def coords_max(coords):
    m = [0, 0]
    for c in coords:
        m[0] = max(m[0], c[0])
        m[1] = max(m[1], c[1])
    return m

def compare_coords(a, b):
    if a[1] < b[1]:
        return -1
    elif b[1] < a[1]:
        return 1
    elif a[0] < b[0]:
        return -1
    elif b[0] < b[0]:
        return 1
    else:
        return 0

# shuffle
def fisher_yates(a):
    n = len(a)
    for i in range(n - 1):  # i from 0 to n-2, inclusive.
        j = randrange(i, n)  # j from i to n-1, inclusive.
        a[i], a[j] = a[j], a[i]  # swap a[i] and a[j].

# shuffle
def sattolo(a):
    n = len(a)
    for i in range(n - 1):
        j = randrange(i+1, n)  # i+1 instead of i
        a[i], a[j] = a[j], a[i]

def neunundvierzig():
    return list(range(1, 50))

def compare_list_recurs(x, y):
    if len(x) < 1:
        return 0

    idx = 0
    while idx < len(x) and idx < len(y):
        if x[idx] < y[idx]:
            return -1
        elif x[idx] > y[idx]:
            return 1
        else:
            idx += 1
    return len(x) > len(y)

NL_REG = re.compile(r"(\A|\n)(.)", re.MULTILINE)
def indent(s, level = 1):
    i = ''
    for _ in range(0, level):
        i += '    '
    return re.sub(
            NL_REG,
            "\\1" + i +"\\2", 
            s
            )

def calc_coord(n):
    if n < 1 or n > 49:
        raise ValueError("out of range")
    y = int((n-1)/7)
    return [(n - y * 7 - 1) % 7, y]

def sorted_coords(coords):
    return sorted(coords, key=cmp_to_key(compare_coords))

# there is probably numpy stuff for this, but it's simple
def coords_lt(a, b):
    return a[0] < b[0] or a[1] < b[1]

def coords_le(a, b):
    return a == b or a[0] < b[0] or a[1] < b[1]

def coords_add(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def coords_sub(a, b):
    return [a[0] - b[0], a[1] - b[1]]

def coords_positive(a):
    return not coords_lt(a, [0,0])


