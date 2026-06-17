# determine memory size of a numpy array
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.nbytes)#memory size in bytes
print(arr.itemsize) #size of each element in bytes i.e in this case 40/5 = 8 bytes
print(arr.size) #number of elements in the array