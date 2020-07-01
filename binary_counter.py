#Code in here counts the number of ones in the binary representation of a number 
#For instance, code will convert two into 10 and print out that it has one '1'

#Step one, take in a number from the user and make sure that the number is an integer
while True:
    user_number = input('Please enter number: ')
    try:
        user_number_int = int(user_number)
        break
    except ValueError:
        print('Please only enter integer number')
        #Jump to the top of the loop to try again
        continue

