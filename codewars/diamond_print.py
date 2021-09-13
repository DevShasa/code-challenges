'''
Description:
Jamie is a programmer, and James' girlfriend. She likes diamonds,
and wants a diamond string from James. 
Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen,
using asterisk (*) characters. 
Trailing spaces should be removed, 
and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, 
as it is not possible to print a diamond of even or negative size.

Examples

diamond(5)
  *
 ***
*****
 ***
  *

diamond(3)
 *
***
 *
'''

def odd(n):
    '''
    Generates an array, each number in the array
    Is the number of '*' that will be in every row
    '''
    oddnos = []
    for num in range(1, n+1):
        if num % 2 != 0:
            oddnos.append(num)

    for x in range(n-1, 0, -1):
        if x % 2 !=0:
            oddnos.append(x)
    
    return oddnos
    
def diamond(n):
    if n % 2 == 0 or n < 0: 
        return None

    rock = ""
    for num in odd(n):
        rock += " "*int((n-num)/2) 
        for x in range(num):
            rock += "*"
        rock += "\n"
    
    return rock

print(diamond(5))
print(diamond(3))

