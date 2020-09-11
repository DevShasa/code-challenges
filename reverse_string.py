def reverse_word(text):
    '''
    Function takes a word and reverses it
    Len() gets the length of the string
    Loop takes the last digit in the string, saving it into...
    .. the first position in the string reversed_text
    '''
    text_reverse = text
    # Get the lenght of the text
    text_lengh = len(text_reverse)
    # Initialise an empty variable where the reversed text will go
    reversed_text = ''

    # Reverse the text using a while loop
    while text_lengh > 0:
        # Code below places letters into the new variable beginning with...
        # ...the last letter of the text
        reversed_text = reversed_text + text_reverse[text_lengh - 1]
        text_lengh = text_lengh - 1

    return reversed_text

# Activating the function


print('The reversed word is')
print(reverse_word("asdft"))
