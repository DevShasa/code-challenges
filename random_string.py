#Code to generate list of random string 
#First create a list with the alphabet
#Then generate random string 
#Then save the strings into a file  
import random

#STEP ONE: create a list with letters 
letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

#STEP TWO, generate random string and save them in a file
#Create an object that enables us to save in a file 
output_file = open('random_words.txt','w')

#Outer loop iterates a hundred times, saving a random string in the file 
for count in range(0,100):
    #Clear the variable 
    rw = ''
    #Inner loob builds the word, the number of iterations is the lenght of the word
    for count in range(0,20):
        #Pick a random letter 
        random_letter = random.randint(0,len(letters)-1)
        #Buld the string  
        rw =  rw + letters[random_letter]
    #Print the string 
    print(rw)
    #Save the string in a file
    file_line = rw +'\n'
    output_file.write(file_line) 

#Close the file 
output_file.close()