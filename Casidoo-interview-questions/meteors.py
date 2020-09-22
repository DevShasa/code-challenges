'''
My first attempt at completing this challenge from Cassidy william's newsletter
Will make improovements as I figure it out
Given an array of integers representing asteroids in a row,
for each asteroid, the absolute value represents its size,
and the sign represents its direction (positive = right, negative = left).
Return the state of the asteroids after all collisions
(assuming they are moving at the same speed).
If two asteroids meet, the smaller one will explode.
When they are the same size, they both explode.
Asteroids moving in the same direction will never meet.
'''

meteors = [2, 4, -5]

for x in meteors:
    # Find the negative number
    if x < 0:
        m = x
for i in meteors:
    # Find the collisions
    if i > 0:
        print(i, 'collides with', m)
        
