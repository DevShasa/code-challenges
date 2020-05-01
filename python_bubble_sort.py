#Demonstration of bubble sort to sort numbers 
'''
First begin by inputting numbers into a list 
The sort numbers in the list using a for loop
Nested if statements inside the for loop will compare two numbers and switch them in order to sort the list 
'''
#Activate the list 
sort_list = [1,34,56,7,3,2,6,678,245,4,2,5,76,87,4]

# #Input ten numbers to sort into a list 
# for input_count in range(1,11):
#     prompt = "Please enter the " +str(input_count)+ " Number: "
#     number_input = input(prompt)
#     sort_list.append(number_input)

#Test that code to input stuff is working
print("The unsorted list is") 
print(sort_list)

#Sort the list from lowest to highest using bubble sort 
for outside_count in range(0, len(sort_list)+1):
    for inside_count in range(0, len(sort_list)-1):
        if sort_list[inside_count] > sort_list[inside_count+1]:
            #If the value on the left is bigger than the value on the right, switch them 
            temp = sort_list[inside_count]
            sort_list[inside_count] = sort_list[inside_count+1]
            sort_list[inside_count+1] = temp

#Lets see if it works shall we 😰
print("The sorted list is")
print(sort_list)
