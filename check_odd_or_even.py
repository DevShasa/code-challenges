#This code checks if a number is odd or even

#Accept user input and validate it to ensure that it is a number
while True:
    try:
        usr_input = input("Please enter a number: ")
        int_usr_input = int(usr_input)
        #If everything goes well break the loop 
        break
    except ValueError:
        #If the user enters something other than a number, perform these statements 
        print("Please only enter a number")
        continue

#This is where we check whether the number is odd or even 
#Use the modulo operator which returns the remainder of a division 
#When even numbers are divided by two they have no remainder,
#If a number has no remainder it is even 
#If a number has a remainder, it is odd 

if (int_usr_input % 2)==0:
    print('The number', int_usr_input,'is an even number')
else:
    print('The number', int_usr_input, 'Is an odd number')