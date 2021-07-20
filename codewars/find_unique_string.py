''' 
There is an array of strings, all strings contain similar letters 
...exept one, try to find it  

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
'''

def find_common(arr):
    for x in range(len(arr)):
        if set(arr[x].lower()) == set(arr[x+1].lower()):
            return set(arr[x].lower())
    return False

def find_uniq(arr):
    for x in arr:
        if set(x.lower()) != find_common(arr):
            return x


