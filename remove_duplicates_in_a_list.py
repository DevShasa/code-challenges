#Go through a list and eliminate duplicates
#TODO, fix bug that makes it no return anything 😭

#First step, create a list with some duplicate values in it 
list_with_duplicates = ["a","f","a","h","w","h","x","x","t","t","n","n","l","l","l","a","f","f","q","t","h"]

#Create a new list that will hold the sorted list withoud duplicates
new_sorted_list = []

#Go through the list checking for duplicates and eliminate duplicates
for list_item in list_with_duplicates:
    if list_item not in list_with_duplicates:
        new_sorted_list.append(list_item)

print('the unsorted list is')
print(new_sorted_list)
