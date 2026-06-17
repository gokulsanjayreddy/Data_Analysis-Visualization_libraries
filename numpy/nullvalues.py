#remove rows with null values in a numpy array
import numpy as np  
a = np.array([[1,2,3],[4,np.nan,6],[7,8,9],[10,11,np.nan],[13,14,15]])
print(a)
print(np.isnan(a)) 
print(np.isnan(a).any(axis=1)) #returns rows with null values
print(a[~np.isnan(a).any(axis=1)]) # ~ is used to avoid rows with null values