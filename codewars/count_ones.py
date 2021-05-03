'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

def sumOfOnes(num):
    return len([i for i in bin(num) if i == "1"])

def countOnes(left, right):
    # one_list = []
    # for i in range(left, right+1):
    #     one_list.append(sumOfOnes(i))
    
    # return sum(one_list)
    return sum([sumOfOnes(i) for i in range(left, right+1)])

