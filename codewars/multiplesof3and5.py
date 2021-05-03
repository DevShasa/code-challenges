'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
'''
def solution(number):
    # List all natural numbers
    natural_numbers = []
    for count in range(1,number):
        if (count % 3 == 0) or (count % 5 == 0):
            natural_numbers.append(count)

    return sum(natural_numbers)

'''Solution that does not build an iteratable'''
def no_list_solution(number):
    summ = 0
    for count in range(number):
        if (count % 3 == 0) or (count % 5 ==0):
            summ += count
    return summ

'''One liner for the win'''
def one_liner_solution(number):
    '''
    Using list comprehension
    '''
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])