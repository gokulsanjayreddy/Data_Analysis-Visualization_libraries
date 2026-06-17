# interpolation
import pandas as pd
data = {
    "Name": ['Ram', 'Shayam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, None, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, None, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, None, 95, 80, 89]
}
df = pd.DataFrame(data)
# by default axis is 0 in case of interpolation
df['Age'] = df['Age'].interpolate(method='linear') #replacces the nan values in the age column in a linear form
print(df)
# there are many types of interpolation methods like polynomial,time etc.......