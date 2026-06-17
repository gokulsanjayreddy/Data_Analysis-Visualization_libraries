# merging two data frames on the basis of columns 
# pd.merge(df1, df2, on="Column_Name", how="type_of_join")
import pandas as pd

# customer dataframe
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Ramesh', 'Suresh', 'Kalpesh']
})

# order dataframe
df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 4],
    'OrderAmount': [250, 450, 350]
})

# merge
# Example using inner join
df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='outer')
print(df_merged)