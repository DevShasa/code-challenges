# Sort words in a string by number of distinct characters

words = ['Bananas', 'do', 'not', 'grow', 'in', 'Mississippi']
def distinctCharacters(myStr):
    '''
    Returns distinct words in a string
    ''' 
    characters = []
    for character in myStr:
        if character not in characters:
            characters.append(character)
    return len(characters)

def sortByDistinctCharacter(myList):
    sortedList = sorted(myList, key=distinctCharacters)
    return sortedList

print(sortByDistinctCharacter(words))
