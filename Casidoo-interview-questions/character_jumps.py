'''
You have a character who jumps forward n number of units at a time,
and an array representing the road in front of them (where 0 is a 
flat piece of road, and 1 is an obstacle). Return true or false if 
your character can jump to the end without hitting an obstacle in front of them.
        ......EXAMPLE......
        $ characterJump(3, [0,1,0,0,0,1,0])
        $ true // no hits
        ......EXAMPLE TWO.....
        characterJump(4, [0,1,1,0,1,0,0,0,0]) 
        $ false // hits obstacle at position 4
'''

road = [0,1,0,0,0,1,0]
usr_input = input('How many units will the character jump: ')
count = 0
for i in road:
    # Increment the counter 
    count = count + 1
    if count == usr_input:
        # Get the position of i
        if i == 0:
            print('True, no hits')
            break
        elif i == 1:
            print('False, hits obstacle at position', usr_input)
            break

