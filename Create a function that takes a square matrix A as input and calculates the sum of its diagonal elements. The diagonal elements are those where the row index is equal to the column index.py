import numpy as np
def sum_diagonal(A):
    sum = 0
    rows = len(A)
    for i in range(rows):
        sum += A[i][i]
    return sum

A = np.array(([[1,2,3], 
              [4,5,6],
              [7,8,9]]))
print(sum_diagonal(A))