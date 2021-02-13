'''
Given an array of integers arr,
a pair (n,m) is called “special” if arr[n] == arr[m]
Return the number of special pairs.
......EXAMPLE
$ specialPairs([1,2,3,1,1,3])
$ 4 // (0,3), (0,4), (3,4), (2,5)
'''
from collections import defaultdict


def count_pairs(xs):
    seen = defaultdict(int)
    count = 0
    for x in xs:
        # Everytime the value of a key increments...
        # ...Count increases
        count = count + seen[x]
        seen[x] = seen[x] + 1
    return count


# Activating the function
array_of_integers = [1, 2, 3, 1, 1, 3]

print(count_pairs(array_of_integers))
