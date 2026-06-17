import pandas as pd
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}
df = pd.DataFrame(data)
# selecting single column
name = df['Name']
print(name)
# selecting multiple columns
names = df[['Name','Salary']]
print(names)
# filtering rows based on single condition
high_salary = df[df['Salary']> 50000]
print(high_salary)
# filtering rows based on multiple conditions
filtered = df[(df['Salary']>30000) & (df['Age']>30)]
print(filtered)
# filtering using or condition
filtered_or = df[(df['Salary']>30000) | (df['Age']>30)]
print(filtered_or)