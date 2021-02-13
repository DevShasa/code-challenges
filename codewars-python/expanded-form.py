'''
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
'''

def expanded_form(num):
    num_str = str(num)
    num_len = len(num_str)
    expanded_form = []
    for i in num_str:

        expanded_number = i
        for x in range(num_len -1):
            expanded_number += '0'
        
        if int(expanded_number) > 0:
            expanded_form.append(expanded_number)

        num_len -= 1

    
    return ' + '.join(expanded_form)


        
'''
refactored into a more elegant solution
'''
def elegant_expanded_form(num):
    result = []

    for index, number in enumerate(reversed(str(num))):
        if int(number) > 0:
            result.append(number + ('0' * index))

