# multiply a str element within a numpy array
import numpy as np
a = np.array(['Gokul','sanjay'])
print(a)
np.char.multiply(a, 2)#function to multiply each element of the array by 2
print(np.char.multiply(a, 2))