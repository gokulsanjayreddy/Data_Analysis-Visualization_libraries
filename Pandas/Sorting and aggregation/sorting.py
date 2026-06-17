# sorting data
# sorting data in 1 column ---> sort_values()
import pandas as pd
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 22, 34, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}
df = pd.DataFrame(data)
df.sort_values(by='Age',ascending=False,inplace=True)#sorts the data based on the age of the persons in the descending order
print(df)
# to sort data based on multiple columns pass a list in place of a single column 
# also pass a list of boolean values in ascending list 