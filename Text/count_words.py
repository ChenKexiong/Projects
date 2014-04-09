# count words in a string
from collections import defaultdict as dt
import operator

def count_words(s):
    words = s.split()
    counts = dt(int)
    for w in words:
        counts[w] += 1
    return counts
if __name__ == '__main__':
    s = raw_input('Input a string:\n').lower()
    counts = count_words(s).items()
    sorted_counts = sorted(counts,key=operator.itemgetter(1),reverse = True)
    mycounts = sorted_counts[:5]
    print mycounts
