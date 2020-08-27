import random
import copy
# Demonstration of bubble sort to sort numbers
'''
First begin by inputting numbers into a list
The sort numbers in the list using a for loop
Nested if statements inside the for loop will compare two numbers...
... and switch them in order to sort the list
'''
# Activate the list
sort_list = []


# Create ten random numbers and save them into a list
for number in range(0, 11):
    random_number = random.randint(1, 100)
    sort_list.append(random_number)


# Test that code to input stuff is working
print("The unsorted list is")
print(sort_list)

# Copy the list into a new list for the sort high to low loop
new_list = copy.deepcopy(sort_list)

# Sort the list from lowest to highest using bubble sort
for outside_count in range(0, len(sort_list)+1):
    # Create a flag that terminates the loop when...
    # ...there are no more comparisons to make,
    # Use of flag makes it a bit more efficient
    flag = False
    for inside_count in range(0, len(sort_list)-1-outside_count):
        if sort_list[inside_count] > sort_list[inside_count+1]:
            temp = sort_list[inside_count]
            sort_list[inside_count] = sort_list[inside_count+1]
            sort_list[inside_count+1] = temp
            flag = True
    # If there are no more comparisons to make break the loop
    if flag == False:
        break

# Sort the list from highest to lowest
for count2 in range(0, len(new_list)+1):
    flag2 = False
    for count3 in range(len(new_list)-1-count2):
        if new_list[count3] < new_list[count3+1]:
            temp = new_list[count3]
            new_list[count3] = new_list[count3+1]
            new_list[count3+1] = temp
            flag2 = True
    if flag2 == False:
        break


# Lets see if it works shall we 😰
print("The list sorted from lowest to highest")
print(sort_list)


print('The list sorted from highest to lowest is')
print(new_list)
