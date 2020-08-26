# Given an array of random integers
# Move all the Zeros in the array to the back
# [0456345] becomes [4563450]

# Create an array with some zeros
array = [1, 3, 6, 0, 4, 6, 0, 5, 7, 0, 5, 7, 0, 6]

# Function to rearrange the digits in the array


def zeroes_back(list_with_zero):
    '''
    Function rearranges a list moving zeroes to the back
    The first while loop gets all the nonzero numbers and puts them first
    The second while loop places the zeroes at the back of the array
    '''
    # The new list will be saved into 'o'
    o = []
    while True:
        # Get the nonzero numbers first placing them first in the new list
        # Once there are no more nonzero numbers quit the while loop
        for x in list_with_zero:
            if x != 0:
                o.append(x)
        break
    while True:
        # Get the remaining zeroes in the list, placing them last
        # Once there are no more zeroes quit the while loop...
        # ...and return the rearranged list
        for y in list_with_zero:
            if y == 0:
                o.append(y)
        break
    return o

# Activating the function


new_array = zeroes_back(array)
print(new_array)