'''
A more concise way of reversing a string
'''
def reverse_string(string):
    reversed_str = ''
    for i in reversed(string):
        reversed_str += i
    return reversed_str

# Activating the function
print(reverse_string('wolan'))
