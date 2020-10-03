# Go through a list and eliminate duplicates using the naive method
# generate random duplicate list entries for list_with_duplicates
# First step, create a list with some duplicate values in it
list_with_duplicates = ["a","f","a","h","w","h","x","x","t","t","n","n","l","l","l","a","f","f","q","t","h"]

def removeDuplicates(duplicateList):
    # Create a new list that will hold the sorted list withoud duplicates
    new_sorted_list = []
    # Go through the list checking for duplicates and eliminate duplicates
    for list_item in duplicateList:
        if list_item not in new_sorted_list:
            new_sorted_list.append(list_item)
    return new_sorted_list


# Activating the function 
result = removeDuplicates(list_with_duplicates)
print(result)