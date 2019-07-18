import sys
import os
import re

from datetime import datetime

#
# Logfile ~/.quicktipp.log
#

# Log tipps and skipps to a log file for later analysis. See if you might have
# won with a skip or something.
def write_to_journal(q):
    try:
        with open(_filename(), "a") as journal:
           journal.write(write_to_journal_str(q, datetime.now()))
    except Exception as e:
        sys.stderr.write('Failed to write journal: ' + str(e) + "\n")

# Find a previous tipp or skip by numbers. numbers_str: "1,2,3,4,5,6"
def find_in_journal(numbers_str):
    numbers = numbers_str.split(',')
    with open(_filename(), "r") as journal:
        for line in journal:
            finding = find_in_journal_str(line, numbers)
            if finding:
                print(finding)

def _num_join(numbers):
    return ' '.join(['%2d' % n for n in numbers])

def _filename():
    return os.environ['HOME'] + "/.quicktipp.log"

def write_to_journal_str(q, now = datetime.now()):
    s = ''
    prefix = now.isoformat() + ': '
    for skipped in q.get_skipped():
        s += prefix + "skipped "+ _num_join(skipped.get_numbers()) + " " + skipped.get_reason() + "\n"

    for tipp in q.get():
        s += prefix + "tipp    "+ _num_join(tipp.numbers()) + "\n"

    return s

def find_in_journal_str(line, numbers):
    if not line.strip():
        return False
    numpart = line.split(': ')
    if len(numpart) != 2:
        return False
    numpart = [int(nstr) for nstr in re.split(r"\s+", numpart[1].strip(), 6) if nstr.isdigit()]
    matches = sum(int(num) in numpart for num in numbers)
    if matches >= 4:
        return line.rstrip() + ' (%d matches)' % matches

