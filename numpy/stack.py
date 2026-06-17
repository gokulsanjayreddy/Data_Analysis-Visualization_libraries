# stacking numpy arrays together
import numpy as np  
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack((a, b)))#stack vertically
print(np.hstack((a, b)))#stack horizontally
print(np.concatenate((a, b)))

