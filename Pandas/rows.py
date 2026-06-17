# for analysing the rows it is impractical to use the whole dataset, so we will use a sample of it
# we use the head() method to get the first 5 rows of the dataset
# we can also use the tail() method to get the last 5 rows of the dataset
import pandas as pd
df = pd.read_json('sample_Data.json',encoding='latin1')
print(df.head(10))#first 10 rows
print(df.tail(10))#last 10 rows