#delete a colomn and  insert a new one in it's place
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(np.delete(a,1,axis=1)) #deletes the second column
b = np.array([[10]])#expands(vertically) and then inserts
print(np.insert(a,1,b,axis=1)) #insert the new column in the place of the old one 
