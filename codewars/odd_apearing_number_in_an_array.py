'''
Given an array of integers, find the one that appears an odd number of times
There sill always be one integer that appears an odd number of times
'''

def find_it(seq):
    # for number in seq:
    #     if seq.count(number) % 2 != 0:
    #         return number
    
    return [number for number in seq if seq.count(number) % 2 != 0][0]
