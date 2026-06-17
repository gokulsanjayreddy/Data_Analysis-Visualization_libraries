#change the array in such a way that it starts with the last row and ends with the first row
import numpy as np
a = np.arange(16).reshape(4,4)#arranges and then reshapes as an array
print(a)
print(a[::-1])#reverses the order of rows in the array and prints