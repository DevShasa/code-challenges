'''
Write a function to find the longest common prefix 
in an array of strings

$ longestPrefix(["cranberry","crawfish","crap"])
$ "cra"

$ longestPrefix(["parrot", "poodle", "fish"])
$ ""
'''
def longestPrefix(words):
    shortest_word = min(map(len, words))

    # Iterate through each word and character
    for letter in range(shortest_word):
        for word in range(1, len(words)):
            if words[0][letter] != words[word][letter]:
                return words[0][:letter]



print(longestPrefix(["parrot", "pardle", "fish"])) 



# Function that takes in two strings and returns the prefix
def prefixTwo(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    i, j = 0, 0
    prefix = ''

    while i <= l1 -1 and j <=l2 -1:
        if str1[i] !=  str2[j]:
            break
        prefix += str1[i]
        i += 1
        j += 1
    return prefix 

print(prefixTwo("cranberry","crawfish"))