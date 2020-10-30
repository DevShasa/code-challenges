# Given an integer array arr, sort the integers in arr...
# in ascending order by the number of 1’s in their binary..
# representation and return the sorted array.
# ............EXAMPLE.........
# $ sortBits([0,1,2,3,4,5,6,7,8])
# ...result----->[0,1,2,4,8,3,5,6,7]
def countOnes(binary_number):
    '''
    This function converts a number into its binary representation
    Thefunction then counts the number of ones and returns that number
    '''
    # Convert the number into its binary representation
    binary_representation = bin(binary_number)
    # Count the number of ones in the binary representation
    count = 0
    for i in binary_representation:
        if i == '1':
            count = count + 1

    return count


def sortByOnes(array):
    '''
    This function takes an array and then rearranges it
    Array is rearranged based on the number of ones in binary representation
    '''
    sortedArray = sorted(array, key=countOnes)
    return sortedArray


# Activating the functions
array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
sorted_number = sortByOnes(array)
print(array)
print('After sorting')
print(sorted_number)
