# adding columns in the data
import  pandas as pd 
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}
df = pd.DataFrame(data)
print(df)#prints the initial data
# creating a new column and passing the data
df['bonus'] = df['Salary']*0.1 #adds a column named bonus
print(df)# prints the modified data

# using insert method
df.insert(0,'ID',[1,2,3,4,5,6,7,8])
print(df)