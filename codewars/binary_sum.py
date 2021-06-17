'''
Implement a function that adds two numbers together 
and returns their sum in binary 
The conversion can happen before or after the addition 
'''

def add_binary(a, b):
    return str(bin(a+b))[2:]

print(add_binary(51,12))