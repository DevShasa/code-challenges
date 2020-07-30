def odd_or_even(number):
    '''
    Function uses the modulo operator to check if odd or even 
    If number is even it returns true if odd it returns false
    '''
    if (number % 2)==0:
        #Number is even, return true 
        return True
    else:
        #Number is odd return false
        return False
    
#Take in number from user and validate it 
while True:
    try:
        pass
        user_input = input('Enter number to check if odd or even: ')
        number = int(user_input)
        break
    except ValueError:
        print('Please only enter a number')
        continue

#Check if number is odd or even by passing it to the odd_or_even function
result = odd_or_even(number)
if result == True:
    print (number, 'Is an even number')
else:
    print(number, 'Is an odd number')