import pandas as pd 
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print(df)
df.to_csv('output.csv', index=False)#these help to create an output file or modify an existing file in the directory
df.to_excel('output.xlsx', index=False)#index = false is taken to aviod the index column containing 0,1,2,3,...
df.to_json('output.json', orient='records')#index = false does not work for json files 
