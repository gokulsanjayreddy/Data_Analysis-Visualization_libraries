#put values from a numpy array over the values of another numpy array at certain positions
import numpy as np
a = np.array([[1,2,3,4,5]]) 
b = np.array([[10,20,30,40,50]])
a.put([1,2,3,4,0],b)#put the vaalues of b in a in the specified positions
print(a)
