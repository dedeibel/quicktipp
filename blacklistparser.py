import re
from transformations import *
from blacklistitem import BlacklistItem, BlacklistItemDirect
from constants import MAX_COORD

from helper import calc_coord

# Parses tipp blacklist patterns from a visual ascii representation. For
# example:
#
# """
# name pyramid-a
# transform R, L, F
# missing 1
# ..x
# .xxx
# x...x
# """
#
# Dots are ignored, x marks numbers.
# 
# misses: Amount of coords that don't have to match  
# transformations: List of transformations that should be applied to the
# pattern before testing. L, R - Rotate, F - Flip, M - Mirror, LM - Left then
#                         Mirror , RM - Right then Mirror
class BlacklistParser:
    transformations = {
            'L90':   L90(),
            'L180':  L180(),
            'R90':   R90(),
            'R180':  R180(),
            'M':     Mirror(),
            'ML90':  ML90(),
            'ML180': ML180(),
            'MR90':  MR90(),
            'MR180': MR180(),
            }

    def parse(pattern):
        coords = []
        lines = pattern.splitlines()
        misses = 0
        name = ''
        transform = []
        direct_numbers = []

        y = 0
        min_x = MAX_COORD
        for line in lines:
            line = line.strip()
            if not line:
                continue
            result = re.match(r'\s*numbers\s+(.+)', line)
            if result:
                direct_numbers = result.group(1).split(',')
                direct_numbers = [int(number) for number in direct_numbers]
                continue
            result = re.match(r'\s*miss(?:es|ing)\s+(\d+)', line)
            if result:
                misses = int(result.group(1))
                continue
            result = re.match(r'\s*name\s+(.+)', line)
            if result:
                name = result.group(1)
                continue
            result = re.match(r'\s*transform\s+(.*)', line)
            # Note: ignore transform config, apply them all now and filter
            # duplicates later
            if result:
                transform.extend(BlacklistParser.transformations.values()) 
                continue
            #    transform_suffixes = result.group(1).split(',')
            #    for transformation_suffix in transform_suffixes:
            #        transformation_suffix = transformation_suffix.strip()
            #        transform.append(BlacklistParser.transformations[transformation_suffix])
            #    continue

            x = 0
            for char in line:
                if char == " " or char == "\t":
                    continue
                elif char == 'x' or char == 'X':
                    min_x = min(min_x, x)
                    coords.append([x, y])
                    x += 1
                elif char == '.':
                    x += 1
                else:
                    raise ValueError("Unexpected chars in line: '%s' (%s)" % (line, name))
            y += 1

            if x > 7 or y > 7:
                raise ValueError("Coords out of bounds: %dx%d (%s)" % (max(0, x - 1), y - 1, name))

        if direct_numbers:
            return BlacklistItemDirect(name, direct_numbers, misses)
        else:
            return BlacklistItem(name, coords, misses, transform)

