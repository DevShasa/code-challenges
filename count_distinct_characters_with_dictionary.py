# Count the characters in a string using a dictionary
def countDistinctCharacters(character_string):
    '''
    Function counts the distinct characters in a string
    '''
    # Initialise the dictionary
    character_dictionary = {}
    for character in character_string:
        dictionary_keys = character_dictionary.keys()
        # Check if the character is in the keys
        if character in dictionary_keys:
            # Increment the dictionary by one using the jey
            character_dictionary[character] += 1
        else:
            # The character is not in the dictionary key so..
            # Create a new dictionary key and set the initial value to one
            character_dictionary[character] = 1
    return character_dictionary


# Activating the function
character_count = countDistinctCharacters('AAATTTYyYY')
print(character_count)

'''
This is a concise one liner solution
'''
def count(string):
    return{i: string.count(i) for i in string}