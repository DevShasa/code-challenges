# In an array of numbers
# Identify the number that appears an odd number of times
def count_odd(arrayOfNumbers):
    # get length of array
    a_size = len(arrayOfNumbers)

    # Outer for loop
    for i in range(0, a_size):
        count = 0
        for x in range(0, a_size):
            # Compare the values
            if arrayOfNumbers[i] == arrayOfNumbers[x]:
                # Increment counter
                count = count + 1
        # Check if the number of appearances is odd
        if (count % 2) != 0:
            # If the result is not equal to zero, the number is odd
            print(arrayOfNumbers[i], 'appears an odd number of times')
            break


# Activating the function
numbers = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
count_odd(numbers)
