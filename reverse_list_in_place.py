
import math
def reverse_list_in_place(lst):
    for i in range(math.floor(len(lst)/2)):
        temp = lst[i]
        lst[i] = lst[len(lst) - 1 - i]
        lst[len(lst) - 1 - i] = temp
    return lst