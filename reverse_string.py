#TODO, write a function in python that reverses a string

string_input = input("Enter word to reverse here: ")

#Get the length of the string 
length_string = len(string_input)

#Process to reverse string 
reverse_text = ''

while length_string > 0:
    reverse_text = reverse_text + string_input[length_string -1]
    length_string = length_string -1 

print("The reversed string is>> ", reverse_text)