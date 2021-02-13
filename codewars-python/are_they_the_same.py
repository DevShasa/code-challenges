'''
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) 
that checks whether the two arrays have the "same" elements, with 
the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, 
regardless of the order.
'''



def comp(array1, array2):
    '''
    This solution works fine but generates an error if the...
    argyments passed as parameters is None type 
    '''
    return sorted([x*x for x in array1]) == sorted(array2)

def comp2(array1, array2):
    '''
    This solution deals with None inputs
    '''
    if array1 == None or array2 == None:
        return False
    return sorted([x*x for x in array1]) == sorted(array2)

def comp3(array1, array2):
    '''
    This solution deals with the Nonetype error using a try catch 
    statement 
    '''
    try:
        return sorted([x*x for x in array1]) == sorted(array2)
    except:
        return False

def comp4(array1, array2):
    '''
    One liner for the win
    '''
    return None not in (array1,array2) and [i*i for i in sorted(array1)]==sorted(array2)
    '''
    the return statement is akin to 
    if None not in (array1,array2) and [i*i for i in sorted(array1)]==sorted(array2): 
        return true:
    else:
        return False
    '''

