'''
Complete the method/function so that it converts dash/underscore
delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).
'''
def to_camel_case(text):
    #your code here
    ntxt = text.replace("_", "-")
    
    text_list = ntxt.split("-")
    
    return_string = ''
    count = 0
    for x in text_list:
        if count == 0:
            return_string += x
        else: 
            return_string += x.title()
        
        count += 1
    
    return return_string
