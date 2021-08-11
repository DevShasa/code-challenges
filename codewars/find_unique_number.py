'''There is an array with some numbers
All numbers are equal except for one, find import

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

'''
def find_common(arr):
    # Find the common number
    count = 0
    for x in range(len(arr)):
        if arr[x] ==  arr[x+1]:
            return arr[x]
    return False
        
def find_uniq(arr):
    # Find the uncommon number
    common = find_common(arr)
    for x in arr:
        if x != common:
            return x
    return False

# THis solution works but takes too long
def find_uniq2(arr):
    return [ x for x in arr if arr.count(x) == 1 ][0]

# The cool solution
def find_uniq3(arr):
    a,b = set(arr)
    return a if arr.count(a) == 1 else b

