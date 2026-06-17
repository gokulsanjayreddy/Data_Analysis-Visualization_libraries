# merging two dataframes either vertically or horizontally
''' vertically - row wise 
    horizontally - column wise'''
import pandas as pd

# Creating sample DataFrames for vertical and horizontal concatenation
df_Region1 = pd.DataFrame({
    'CustomerID': [1, 2],
    'Name': ['Gopal', 'Raju']
})

df_Region2 = pd.DataFrame({
    'CustomerID': [3, 4],
    'Name': ['Shyam', 'Baburao']
})

# 1. Vertical Concatenation (axis=0)
# This stacks the DataFrames on top of each other.
df_concat_vertical = pd.concat([df_Region1, df_Region2], axis=0, ignore_index=True)
print("Vertical Concatenation:\n", df_concat_vertical)

# 2. Horizontal Concatenation (axis=1)
# This combines the DataFrames side-by-side.
df_concat_horizontal = pd.concat([df_Region1, df_Region2], axis=1)
print("\nHorizontal Concatenation:\n", df_concat_horizontal)