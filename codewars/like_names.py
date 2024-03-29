'''
You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, 
which must take in input array, containing the names of people who like an item. 
It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this
'''
def likes(names):
    if not names:
        return 'no one likes this'
    
    if len(names) == 1:
        return f'{names[0]} likes this'
    
    if len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    
    return f'{names[0]}, {names[1]} and {len(names)-2} others like this'

# An alternative solution that avoids if statements 
def likes2(names):
    return_strings = {
        0: 'no one likes this',
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }
    n = len(names)
    return return_strings[min(4,n)].format(*names, others= n-2)

print(likes2(["Max", "John", "Mark"]))
