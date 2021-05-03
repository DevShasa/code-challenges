'''
A Narcissistic Number is a positive number which is the sum of its own digits,
each raised to the power of the number of digits in a given base. 
In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcisstic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

Your code must return true or false depending upon whether
the given number is a Narcissistic number in base 10.
'''

def narcissistic(value):
    '''
    Determines if a number is nacricistic 
    '''
    
    value_list = [int(i) for i in str(value)]

    for x in range(1,10):
        total = 0
        for i in value_list:
            total += i**x
            if total == value:
                return True
    
    return False

'''
Turns out we just need the sum of the digits to the power of the 
length of the value and not the sum of the entire base 10! sooo
'''
def narcicistic2(value):
    value = str(value)
    sum = 0
    for i in value:
        sum += int(i)**len(value)
    return sum == int(value)

'''
One line solution becoz whainot
'''

def narcicistic3(value):
    return value ==sum(int(x)**len(str(value)) for x in str(value))