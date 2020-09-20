# First attempt creating a fibonacci
def fibonacci(length):
    '''
    Function will print out a fibonacci sequence
    parameter 'length' is how long the sequence is
    Because the first two numbers are generated...
    ... lenght will be lenght +2
    Function will also print out lenght as the nth number
    '''

    # Create the seed numbers
    seed = [0, 1]
    # The for statement that generates the fibonacci sequence
    for x in range(length):
        n = seed[x] + seed[x + 1]
        seed.append(n)
    # Print the sequence
    print(seed)

    # Finding the nth number
    print('The', length, 'number is', seed[length-1])


# Activate the function
fibonacci(9)
