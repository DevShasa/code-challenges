'''
Take in a list of strings, return the largest
'''
def largest_string(string_list):

    dlist = dict()
    largest = 0
    for x in string_list:
        dlist[len(x)] = x

        if len(x) > largest:
            largest = len(x)
    
    return dlist[largest]

    
words = ["apple", "pie", "ishahalongest", "good"]
print(largest_string(words))

# Can it be a one liner? 

def largest_string_one_line(string_list):
    return string_list[[len(x) for x in string_list].index(max([len(x) for x in string_list]))] 

print(largest_string_one_line(words)) # Guess so 
