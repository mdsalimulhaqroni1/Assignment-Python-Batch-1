import numpy as np

def is_identity_matrix(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if i == j:
                if A[i][j] != 1:
                    return False
            else:
                if A[i][j] != 0:
                    return False
    return True

A = np.array(([[1,0,0],
              [0,1,0],
              [0,0,1]]))
print(is_identity_matrix(A))
