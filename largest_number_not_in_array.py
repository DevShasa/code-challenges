
# Find the largest interger not in the array

def largestNotIn(oArr):
    diffArr = []
    for x in range(min(oArr), max(oArr)+1):
        if x in oArr:
            pass
        else:
            diffArr.append(x)
    
    return max(diffArr)

print("LARGEST NUMBER NOT IN ARRAY IS: ",largestNotIn(oArr))
