'''
Sort the given array of strings in alphabetical order, case insensitive. For example:

["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]
'''
def sortme(words):

    word_dict = dict()
    for string in words:
        word_dict[string] = string.lower()

    # output from sorted(word_dict.items(), key=lambda x: x[1]) is ...
    # [('fine', 'fine'), ('Hello', 'hello'), ("I'm", "i'm"), ('there', 'there')]
    return [x[0] for x in sorted(word_dict.items(), key=lambda x: x[1])]

print(sortme(["C", "d", "a", "B"]))
print(sortme(["Hello", "there", "I'm", "fine"])) 

#%%