'''
You’re given a string of characters that are only 2s and 0s.
Return the index of the first occurrence of “2020” without
using the indexOf (or similar) function, and -1 if it’s not
found in the string.

EXAMPLE
>>> find2020(‘2220000202220020200’)
>>> 14
'''

def find2020(string2020):
    '''
    Has improovements over the previous function
    '''
    for x in range(0, len(string2020)-1):
        if string2020[x:x+4] == '2020':
            return x
    return -1

# Activating the function
print(find2020('222000020222002020'))
