#!/usr/bin/python
# count vowls
from collections import defaultdict as dt
def countvowls(s):
    counts = dt(int)
    v = ['a','e','i','o','u']
    for c in s:
        if c in v:
            counts[c] += 1
    return counts

if __name__ == '__main__':
    s = raw_input('Input a string:\n').lower()
    print "The vowls in this string are:\n "
    print countvowls(s).items()
