'''
Use binary search to search through an ordered array
'''
#%%
import math
def binarySearch(array, search):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        midpoint = math.floor((upper_bound + lower_bound)/2)
        value_at_midpoint = array[midpoint]

        # If the value is not the midpoint, eliminate half the array 
        if value_at_midpoint ==  search:
            return midpoint
        # The value is on the left side of the array
        # so eliminate the right side of teh array 
        if search < value_at_midpoint:
            upper_bound = midpoint -1
        # The value is on the right side of the array so update lower bound
        if search > value_at_midpoint:
            lower_bound = midpoint + 1
    return False