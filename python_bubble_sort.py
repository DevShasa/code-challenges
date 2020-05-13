import random
import copy
#Demonstration of bubble sort to sort numbers 
'''
First begin by inputting numbers into a list 
The sort numbers in the list using a for loop
Nested if statements inside the for loop will compare two numbers and switch them in order to sort the list 
'''
#Activate the list 
sort_list =[]


#Create ten random numbers and save them into a list
for number in range(0,11):
    random_number = random.randint(1,100)
    sort_list.append(random_number)
  

#Test that code to input stuff is working
print("The unsorted list is") 
print(sort_list)

#Copy the list into a new list for the sort high to low loop
new_list = copy.deepcopy(sort_list)

#Sort the list from lowest to highest using bubble sort 
for outside_count in range(0, len(sort_list)+1):
    for inside_count in range(0, len(sort_list)-1):
        if sort_list[inside_count] > sort_list[inside_count+1]:
            #If the value on the left is bigger than the value on the right, switch them 
            temp = sort_list[inside_count]
            sort_list[inside_count] = sort_list[inside_count+1]
            sort_list[inside_count+1] = temp

#Sort the list from highest to lowest, basicaly the same as above just change the comparison operator
for count2 in range(0,len(new_list)+1):
    for count3 in range(len(new_list)-1):
        if new_list[count3] < new_list[count3+1]:
            #If left digit is smaller than right digit, switch them 
            temp = new_list[count3]
            new_list[count3] = new_list[count3+1]
            new_list[count3+1] = temp



#Lets see if it works shall we 😰
print("The list sorted from lowest to highest")
print(sort_list)


print('The list sorted from highest to lowest is')
print(new_list)

