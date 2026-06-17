# select min valuea long the rows in a numpy array
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.apply_along_axis(lambda x: np.min(x), axis=1, arr=a))#function to select the minimum value along the rows of the array
# here we can also apply loops to select the min value in the array but using the apply_along_axis function is more efficient and faster than using loops.