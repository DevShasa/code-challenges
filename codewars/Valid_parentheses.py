'''
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
'''

def valid_parentheses(string):
    c = 0
    flag = True 
    for x in string:
        if x == "(":
            c += 1
        if x == ")":
            c -= 1
            if c < 0:
                flag = False
    
    if c == 0 and flag == True:
        return True
    else:
        return False

'''
What the refactored solution may look like
'''
def valid_parentheses2(string):
    count = 0
    for item in string:
        if item == "(":
            count += 1
        if item == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0