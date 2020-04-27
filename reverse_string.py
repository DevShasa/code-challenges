
def reverse_word(text):
    '''
    Function takes a word and reverses it 
    Len() gets the length of teh string
    Loop takes the last digit in teh string, saving it into the first position in the string reversed_text
    '''
    text_reverse = text
    text_lengh = len(text_reverse)
    reversed_text = ''

    #Reverse the text using a while loop 
    while text_lengh > 0:
        reversed_text = reversed_text + text_reverse[text_lengh -1]
        text_lengh = text_lengh -1

    return reversed_text

#Activating the function
print('The reversed word is') 
print(reverse_word("asdft"))