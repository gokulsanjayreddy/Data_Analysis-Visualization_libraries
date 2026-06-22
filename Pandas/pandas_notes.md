# Pandas Notes

## Introduction
- **Data Manipulation**: Changing, organizing, or preparing data to make it useful and easier to understand [cite: 1]. Used to clean and structure raw data for better usability [cite: 2].
- **Data Analysis**: Extracting patterns, trends, and insights from the data to solve problems [cite: 3].

## Data Structures
- **Series**: A one-dimensional labeled array that can hold any data type (integers, floats, strings, or even python objects) [cite: 3]. Each element has a unique label called an index [cite: 4]. Used to track changes or patterns over time [cite: 4].
- **Data Frame**: A 2D labeled data structure in Pandas, like a table in a database, Excel spreadsheet, or SQL table [cite: 5]. It has rows and columns [cite: 6].
    - **Rows**: indices (labels) [cite: 6].
    - **Columns**: names (labels) [cite: 6].

## Input/Output
- **Encoding**: Converts text to formats that computers can store and read [cite: 7].
    - Set encoding to styles like `'utf-8'` or `'latin1'` [cite: 7].
    - No need for encoding if it accepts in the first case [cite: 8].
    - *Example*: `df = pd.read_csv("sales_data_sample.csv", encoding='latin1')` [cite: 9].
- **Other Read Functions**:
    - **Excel**: `df = pd.read_excel("File.xlsx")` [cite: 9].
    - **JSON**: `df = pd.read_json("file.json")` [cite: 9].
    - *Note*: File should be in the same directory as the code [cite: 9].
    - **Cloud Data**: Read through specific libraries (e.g., Google Cloud -> `gcfs` library) [cite: 10].
- **Saving Files**:
    - `df.to_csv("Output.csv", index=False)` [cite: 11].
    - `df.to_excel(...)` [cite: 11].
    - `df.to_json(...)` [cite: 11].

## Data Exploration
- **Understanding the Data**: Understand the data set, identify problems, and plan next steps [cite: 12].
- **Analyzing Rows**: Use `head()` and `tail()` for initial and final rows (default 5 rows) [cite: 12].
- **`df.info()`**: Summarizes the data set, including number of rows/columns, memory usage, data types, column names, and non-null values [cite: 13, 14].
- **`df.describe()`**: Prints statistical data (count, mean, std, min, max) [cite: 14].
    - **Quartiles**: 25% (First), 50% (Second), 75% (Third) [cite: 15].
- **Metadata**:
    - `df.shape`: Number of rows and columns [cite: 16].
    - `df.columns`: Names of columns [cite: 16].

## Data Manipulation
- **Selection**:
    - Single Column: `column = df["ColumnName"]` [cite: 17].
    - Multiple Columns: `subset = df[["Column1", "Column2", ...]]` [cite: 17].
- **Filtering Rows**:
    - Single Condition: `filter_rows = df[df["Salary"] > 50000]` [cite: 17].
    - Multiple Conditions: `filter_rows = df[(df["Salary"] > 50000) & (df["Column2"] < 80000)]` [cite: 17].
    - Use `|` for the 'or' condition [cite: 18].
- **Adding/Modifying**:
    - Add Column: `df["Bonus"] = df["Salary"] * 0.1` [cite: 18].
    - Insert Method: `df.insert(location, "ColumnName", somedata)` [cite: 18].
    - Modify Value: `df.loc[Row_index, 'ColumnName'] = NewValue` [cite: 18].
- **Removing**:
    - Drop Columns: `df.drop(columns=["ColName"], inplace=True)` [cite: 18].

## Handling Missing Data
- **Types**: `NaN` (Not a Number, for object types), `None` [cite: 19].
- **Checking**:
    - `isnull()`: Returns Boolean (True if missing) [cite: 20].
    - Count missing: `df.isnull().sum()` [cite: 21].
- **Fixing**:
    - Remove: `df.dropna(axis=0, inplace=True)` (axis 0=rows, 1=cols) [cite: 22].
    - Fill: `df.fillna(value, inplace=True)` [cite: 23].
    - Fill with Mean: `df['cn'] = df['cn'].fillna(df['cn'].mean(), inplace=True)` [cite: 23].
    - Interpolation: `df['cn'] = df['cn'].interpolate(method='linear')` [cite: 24, 25]. Useful for time series and trends [cite: 26].

## Sorting, Grouping, and Merging
- **Sorting**: `df.sort_values(by="cn", ascending=True/False, inplace=True)` [cite: 26]. Pass a list for multiple columns [cite: 27].
- **Aggregation**: `mean()`, `min()`, `max()`, `sum()`, `count()`, `std()` [cite: 28, 32].
- **Grouping**:
    - `obj = df.groupby('cn1')['cn2'].sum()` [cite: 29].
    - Groups based on unique column values [cite: 29]. Pass list for multiple columns [cite: 31].
- **Merging**: `pd.merge(df1, df2, on='cn', how='...')` [cite: 33].
    - Joins: `inner`, `outer`, `left`, `right` [cite: 33, 34, 35].
- **Concatenation**: `pd.concat([df1, df2], axis=0, ignore_index=True)` [cite: 38, 39].
    - `axis=0` (vertical), `axis=1` (horizontal) [cite: 38].
- **Cross Join**: Cartesian product (m * n rows) [cite: 36, 37].
