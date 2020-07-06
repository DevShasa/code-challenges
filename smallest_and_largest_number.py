#This code is for the purpose of finding the largest and smallest number in a list 

#STEP ONE, use python random function to populate the list with ten random numbers 
import random
number_list = []
#Fill the list with ten random numbers between 1 and 100
for count in range(1,10+1):
    random_number = random.randint(1,100)
    number_list.append(random_number)
#Print the list 
print("The ten random numbers are")
print(number_list)

#STEP TWO find the smallest number in the list
smallest_number = number_list[0]
for count1 in number_list:
    if smallest_number > count1:
        smallest_number = count1
print('The smallest number is', smallest_number)
