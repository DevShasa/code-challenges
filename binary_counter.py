# Code counts the number of ones in the binary representation of a number
# For instance, code will convert two into 10 and print out that it has one '1'

# take in a number from the user and make sure that the number is an integer
while True:
    user_number = input('Please enter number: ')
    try:
        user_number_int = int(user_number)
        break
    except ValueError:
        print('Please only enter integer number')
        # Jump to the top of the loop to try again
        continue

# STEP TWO, convert the number to binary using inbuilt pythn function
usr_number_bin = bin(user_number_int)

# STEP THREE, count the number of ones in the binary number using a for loop
# Here we convert to a string so that we can compare each digit in the string
usr_string = str(usr_number_bin)
count = 0
for counter in usr_string:
    # If a digit in the string is 1 increase counter by one
    if counter == '1':
        count = count + 1

# STEP FOUR, print out the result
print('The interger number you entered is', user_number_int)
print('Its binary representation is', usr_number_bin)
print('The number of ones in the binary representation is', count)
