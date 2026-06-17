# remove single dimension entries form a numpy array and check if a number is present in the array or not
import numpy as np
a = np.array([[[1,2,3,4,5],[6,7,8,9,10]]])
print(a.shape) #here we can notice an extra dimension of size 1
print(a)
print(a.squeeze()) #this will remove the extra dimension of one 
print(a.shape)
print(np.isin(4,a))