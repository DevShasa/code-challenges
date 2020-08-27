# Given a string s and a character c..
# Return the number of occurences of C in s
# For instance numChars('chameleon', 'e')

def count_characters(string, character):
    c = 0
    for x in string:
        if x == character:
            c = c + 1
    return c

# Activating the function


occurences = count_characters('chameleon', 'e')
print("The character occurs", occurences, "times")
