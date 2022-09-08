# Find the interger in array A and the integer in array B
# That when added together adds up to K or close
def solution(A, B, K):
    computedArr = []
    for x in range(0, len(A)):
        for y in range(0, len(B)):
            computedArr.append([ A[x] + B[y], [A[x], B[y]]])

    smallest = computedArr[0]
    for n in computedArr:
        # print(n)
        if n[0] > K:
            pass
        else:
            if K - n[0]< K - smallest[0]:
                smallest = n

    return smallest[1]

A = [6, 7, 5, 4]
B = [1, 1, 8, 2]
K = 10 

print(solution(A, B, K)) # returns [7,2]
