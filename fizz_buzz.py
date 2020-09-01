# My attempt to solve the fizz buzz challenge
# Write a program that prints all the numbers from 1 to 100.
# For multiples of 3, instead of the number, print "Fizz"
# for multiples of 5 print "Buzz"
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".

for count in range(1, 100):
    if count % 3 == 0 and count % 5 == 0:
        # The number is a multiple of three and five
        print("Fizz Buzz")
        continue
    elif count % 5 == 0:
        # The number is a multiple of five
        print("Buzz")
        continue
    elif count % 3 == 0:
        # The number is a multiple of three
        print("Fizz ")
        continue
    else:
        print(count)
