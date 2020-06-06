#This code checks if a number is odd or even
#Accept user input and validate it to ensure that it is a number
while True:
    try:
        usr_input = input("Please enter a number: ")
        int_usr_inpur = int(usr_input)
        #If everything goes well break the loop 
        break
    except ValueError:
        #If the user enters something other than a number, perform these statements 
        print("Please only enter a number")
        continue

#This is where we check whether the number is odd or even 