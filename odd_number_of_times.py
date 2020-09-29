# In an array of numbers
# Identify the number that appears an odd number of times 
l = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]

# get length of array 
a_size = len(l)

# Outer for loop 
for i in range(0, a_size):
    count = 0
    for x in range(0, a_size):
        # Compare the values 
        if l[i] == l[x]:
            # Increment counter
            count = count + 1
    # Check if the number of appearances is odd using a modulo operator 
    if (count % 2) != 0:
        # If the result is not equal to zero, the number is odd
        print('The number that appears an odd number of times is', l[i])
        break



