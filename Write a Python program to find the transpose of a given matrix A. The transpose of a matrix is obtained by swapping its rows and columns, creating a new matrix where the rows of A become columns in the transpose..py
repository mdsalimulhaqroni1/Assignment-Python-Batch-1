import numpy as np

def transponse(A):
    rows = len(A)
    cols = len(A[0])
    B = np.zeros((cols, rows))

    for i in range(rows):
        for j in range(cols):
            B[j][i] = A[i][j]
    return B

A =np.array([[1,2,3], [4,5,6]])
print(transponse(A))
