'''
Given a list of numbers and a number k, 
return whether any two numbers in the list add 
up to k

EXAMPLE 
given [10, 15, 3, 7]
k = 17
return true scince 10 + 7 is 17
'''
def add_up_true(l_of_numbers, k):
    for x in range(0, len(l_of_numbers) -1):
        for y in l_of_numbers:
            z = l_of_numbers[x]
            if y + z == k:
                return True

# Do it with tests like a gud boi 
import unittest
class testList(unittest.TestCase):
    # Main test
    def test_list(self):
        self.assertTrue(add_up_true([10, 15, 3, 7], 17))    


# Run the test 
if  __name__ == "__main__":
