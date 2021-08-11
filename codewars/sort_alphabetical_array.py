'''
Sort the given array of strings in alphabetical order, case insensitive. For example:

["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]
'''
def sortme(words):

    word_dict = dict()
    for string in words:
        word_dict[string] = string.lower()
    
    sorted_dict = sorted(word_dict.items(), key=lambda x: x[1])
    sorted_list = []
    for x in sorted_dict:
        sorted_list.append(x[0])
    return sorted_list

print(sortme(["C", "d", "a", "B"]))
print(sortme(["Hello", "there", "I'm", "fine"]))

