# removing columns  in a data frame
import pandas as pd
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}
df = pd.DataFrame(data)
# df.drop(columns = ['column name], inplace= True)
# inplace = false creates a new data frame , but we don't want that so we use inplace = True
df.drop(columns=['Performance Score'], inplace=True)#we can place multiple columns in the list 
print(df)