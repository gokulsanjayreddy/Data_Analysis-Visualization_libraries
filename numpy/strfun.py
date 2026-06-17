#create a numpy program to create  str element in a specified numpy array to uppercase,lowercase and capitalize the first letter , title case or swap case
import numpy as np
a = np.array(['Hello','world','python'])
uppera = np.char.upper(a)
print(uppera)
lowera = np.char.lower(a)
print(lowera)
capitalizeda = np.char.capitalize(a)#capitalize will capitalize the first letter of the string and make the rest of the letters lowercase
print(capitalizeda)
titlea = np.char.title(a)#title doing the same thing as capitalize but it will capitalize the first letter of each word in the string 
print(titlea)
swapcasea = np.char.swapcase(a)#swapcase will swap the case of each letter in the string
print(swapcasea)
