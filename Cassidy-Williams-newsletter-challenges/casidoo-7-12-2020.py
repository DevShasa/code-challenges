'''
This week’s question:
Given two non-negative integers n1 and n2 represented as strings,
return the product of n1 and n2, also represented as a string.
Neither input will start with 0, and don’t just convert it
to an integer and do the math that way.

EXAMPLES
>> stringMultiply(“123”, “456”)
>> “56088”
'''


def string_multiply(num1, num2):
    '''
    Takes in two strings arguments
    Returns the product of the two strings
    '''
    return str(eval(num1+'*'+num2))


# Activating the function
string_multiply('123', '456')
