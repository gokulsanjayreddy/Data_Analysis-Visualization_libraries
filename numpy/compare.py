#compare two numpy arrays
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[9,8,7],[61,5,14],[31,2,1]])
print(a==b)#returns boolean element wise similarly for < and > too
print(a>b)
print(a<b)