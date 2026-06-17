# for filling missing values we use fill na 
# fillna()
# fillna(value,inplace = True)
import pandas as pd
data = {
    "Name": ['Ram', 'Shayam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, None, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, None, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, None, 95, 80, 89]
}
df = pd.DataFrame(data)
# df.fillna( 0, inplace=True) --------> for replacing all values with 0 
# print(df)
# for filling the  nan values in each column we can access each column to change/fill the values 
df['Age']= df['Age'].fillna(df['Age'].mean( ),inplace=True)
# similarly for other columns we can do this 
print(df)