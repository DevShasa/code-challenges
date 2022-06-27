# Given a string and a set of words
# find the longest word in dict that is a subsequence of str

strWord = "abppplee"
setOfWords = ["able", "ale", "apple", "bale", "kangaroo"]

def largestString(strArr):
    '''
    Takes in a string, returns the largest word in the string
    '''
    x = [len(x) for x in strArr]
    maxIndex = x.index(max(x)) # Get index of max item
    return strArr[maxIndex]

def longestSub(strWord, setOfWords):
    uniQueWord = set(strWord)
    similar = []
    for w in setOfWords:
        if set(w).issubset(uniQueWord):
            similar.append(w)
    
    return largestString(similar)

print(longestSub(strWord, setOfWords))


