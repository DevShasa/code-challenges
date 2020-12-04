import random
# A function that returns true if a number is even
# Use a filter statement to filter out odd numbers from a list


def even_true(number):
    '''
    Check whether a number is  even
    Return true if number is even
    '''
    if number % 2 == 0:
        return True


# TEN RANDOM NUMBERS
num_array = []
for count in range(1, 11):
    x = random.randint(1, 9)
    num_array.append(x)

print(f'UNfiltered numbers are {num_array}')

filtered_array = filter(even_true, num_array)
print(f'FIltered array is {list(filtered_array)}')

# The function can be replaced by a lambda function
# filter(lambda number: True if number % 2 == 0 else False, num_array)
