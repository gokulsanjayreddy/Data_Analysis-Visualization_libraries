# create a border line to a 2*2 array
# this border is known as padding of an array and filled with numbers
import numpy as np
a = np.array([[1,2],[3,4]])
print(np.pad(a, pad_width=2, mode='constant', constant_values=0))#set the mode to constant cause we are filling it with a constant value i.e 0