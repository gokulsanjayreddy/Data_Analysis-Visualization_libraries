# find out the missing values and the no of missing values
import pandas as pd 
data = {
    "Name": ['Ram', 'Shyam', None, 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, None, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, None, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, None, None, 95, 80, 89]
}
df = pd.DataFrame(data)
print(df.isnull())# returns boolean value for each item in the df if it is a nan value
print(df.isnull().sum())#prints the no of null values in each column
