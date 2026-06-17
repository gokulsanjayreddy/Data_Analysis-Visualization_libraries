# check if a certain number is present in a numpy array and replace the negative values with a certain number
import numpy as np
a = np.array([[1,2,3],[-4,5,-6],[7,-8,9]])
print(np.isin(a, 5))#check if the number 5 is present in the array
a[a<0] = 6#replace the negative values with 6
print(a)