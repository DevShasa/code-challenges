
'''
Examples 
Given a list of folders in a filesystem and the name of a folder to remove,
return the new list of folders after removal

$ removeFolder([“/a”,”/a/b”,”/c/d”,”/c/d/e”,”/c/f”, “/c/f/g”], ‘c’)
$ [“/a”,”/a/b”]
'''
def remove_folder(list_of_folders, folder_to_remove):
    new_folder_list = []
    for folder_name in list_of_folders:
        flag = True
        for folder_letter in folder_name:
            if folder_letter == folder_to_remove:
                flag = False
        if flag == True:
            new_folder_list.append(folder_name)

    return new_folder_list

# Check if everything works         

print(remove_folder(['/a','/a/b','/c/d','/c/d/e','/c/f', '/c/f/g'], 'c'))

print(remove_folder(['/a','/a/b','/c/d','/c/d/e','/c/f', '/c/f/g'],'d'))
