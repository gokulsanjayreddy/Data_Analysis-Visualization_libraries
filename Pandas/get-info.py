# get all the information about the dataset using the info() method
import pandas as pd
df = pd.read_json('sample_Data.json',encoding='latin1')
print(df.info())
go = pd.read_csv('SampleSuperstore - Orders.csv',encoding='latin1')
print(go.info())