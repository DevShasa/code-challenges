def characterCount(string):
    '''
    Print the number of letters in a string
    '''
    # Create an empty dictionary into which we will save the string
    dictionary = {}
    # Use a for loop to break the dictionary
    for character in string:
        # Create an list of the dictionary keys
        # On the first pass of the loop the dictionary will be empty
        list_of_keys = dictionary.keys()

        # The next step is to check the list of keys above
        # If a letter is not in the keys , assign a default value
        # If a letter is in the keys increment the key value by one
        if character in list_of_keys:
            # Increment the coresponding key valyue by one
            dictionary[character] += 1
        else:
            # If teh code jumps to this statement it means that the
            # Character is not in the dictionary
            # The code in the else statement creates the dictionary key
            # ...then assigns a default valuue of one
            dictionary[character] = 1

    return dictionary

print(characterCount('dictionary'))
