#get row numbers of a numpy array if any element in the row is greater than a specified value
import numpy as np
a = np.array([[17,2,3],[4,50,6],[7,89,9],[-10,121,112],[13,142,15]])
print(a[a>40])
print(np.any(a>40,axis=1)) #this will return a boolean array where each element is True if any element in the corresponding row of the original array is greater than 40
print(np.where(np.any(a>40,axis=1))) #this will return the row numbers where any element is greater than 40
print(np.where(np.any(a>40,axis=0)) )#this will return the column numbers where any element is greater than 40