#Code in here checks if a word is a palindrome 
#A palindrome reads the same from left to right and right to left 
#A function will first reverse an entered word and then compare the reversed word to the original word 

def palindrome_checker(word):
    #STEP ONE, reverse the word
    input_word = word
    #Get the lenght of the word 
    word_lenght =  len(input_word)
    #Initialize empty string to put reversed word 
    reversed_word = ''
    #Use a while loop to reverse the word 
    while word_lenght > 0:
        reversed_word = reversed_word + input_word[word_lenght - 1]
        word_lenght = word_lenght - 1  

    #STEP TWO, compare the two words using if statements 
    if reversed_word == input_word:
        print('The word', input_word, 'Is a palindrome')
    else:
        print('The word', input_word, 'Is not a palindrome')

#Activating the function 
palindrome_checker('madam')