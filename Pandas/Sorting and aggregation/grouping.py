#grouping is done on the basis of a certain column name and certain mathematical operations can be performed
import pandas as pd
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 22, 29, 28, 25, 34],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}
df = pd.DataFrame(data)
grouped = df.groupby('Age')['Salary'].sum()# here items are grouped by age and result is the sum of salaries of that aged employees
print(grouped)