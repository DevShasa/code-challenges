'''
Given an array of integers of any length, return an array 
hat has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]
'''
def up_array(arr):
    number = ""
    for num in arr:
        if num < 0 or type(num) != int or num not in [0,1,2,3,4,5,6,7,8,9]:
            return None
        x = str(num)
        number += x
    
    if number != "":
        plus_one = int(number) + 1
    else:
        return None
    return [int(n) for n in str(plus_one)]

print(up_array([2,3,9]))
