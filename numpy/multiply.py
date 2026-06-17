#multiply two matrices element-wise and matrix multiplication
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[1,7,2],[2,6,5],[3,5,6]])
print(a*b)
print(a.dot(b))#matrix multiplication
print(np.matmul(a,b))