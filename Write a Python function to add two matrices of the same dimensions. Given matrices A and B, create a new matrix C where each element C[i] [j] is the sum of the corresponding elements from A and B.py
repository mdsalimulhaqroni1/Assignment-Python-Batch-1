import numpy as np

def add_matrices(A, B):
  C = np.empty_like(A)
  for i in range(len(A)):
    for j in range(len(A[0])):
      C[i][j] = A[i][j] + B[i][j]
  return C

A = np.array([[1,2], [3,4]]) 
B = np.array([[5,6], [7,8]])

C = add_matrices(A, B)
print(C)
