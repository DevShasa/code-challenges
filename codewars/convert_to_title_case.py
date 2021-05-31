'''
A string is considered to be title case if EACH WORD IN THE STRING IS EITHER 
> capitalised 
> considered to be an exeption and put entirely into lowercase unless it is the first word 

Write a function that will convert a string into title case, given an optional list of exeptions (minor words)
Minor words will be given as a string with each word separated by a space, 
The function should ignore the case of the minor words string
'''

def title_case(title, minor_words=''):
    new_string = []
    count = 0
    for x in title.split(" "):
        y = x.lower()
        # Selectively capitalize the words
        if y in [c.lower() for c in minor_words.split(" ")]: 
            # Check if it is the first word, if it is not CAPITALIZE
            if x == title.split(" ")[0] and count == 0:
                new_string.append(y.capitalize())
                count += 1
            else:
                new_string.append(y)
        else:
            new_string.append(y.capitalize())


    return " ".join(new_string)


# AN optimised solution 

def o_title_case(title, minor_words=""):
    # Capitalize the first word 
    title =  title.capitalize().split(" ")
    minor_words = minor_words.lower().split(" ")
    " ".join([word if word in minor_words else word.capitalize() for word in title])