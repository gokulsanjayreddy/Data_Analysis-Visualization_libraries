#repalce diagonal values in a numpy array with a certain value
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b =np.array([[1,2,3],[4,5,6],[7,8,9]])
np.fill_diagonal(b, 9)#inbuit function replaces the diagonal values with a certain value
for i in range(len(a)):
    for j in range(len(a)):
        if i==j:
            a[i][j] = 0
    
print(a)
print(b)#first execute the function and then print the array