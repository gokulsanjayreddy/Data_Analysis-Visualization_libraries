# Pandas Notes

## Introduction
- **Data Manipulation**: Changing, organizing, or preparing data to make it useful and easier to understand. Used to clean and structure raw data for better usability.
- **Data Analysis**: Extracting patterns, trends, and insights from the data to solve problems.

## Data Structures
- **Series**: A one-dimensional labeled array that can hold any data type (integers, floats, strings, or even python objects). Each element has a unique label called an index. Used to track changes or patterns over time.
- **Data Frame**: A 2D labeled data structure in Pandas, like a table in a database, Excel spreadsheet, or SQL table. It has rows and columns.
    - **Rows**: indices (labels).
    - **Columns**: names (labels).

## Input/Output
- **Encoding**: Converts text to formats that computers can store and read.
    - Set encoding to styles like `'utf-8'` or `'latin1'`.
    - No need for encoding if it accepts in the first case.
    - *Example*: `df = pd.read_csv("sales_data_sample.csv", encoding='latin1')`.
- **Other Read Functions**:
    - **Excel**: `df = pd.read_excel("File.xlsx")`.
    - **JSON**: `df = pd.read_json("file.json")`.
    - *Note*: File should be in the same directory as the code.
    - **Cloud Data**: Read through specific libraries (e.g., Google Cloud -> `gcfs` library).
- **Saving Files**:
    - `df.to_csv("Output.csv", index=False)`.
    - `df.to_excel(...)`.
    - `df.to_json(...)`.

## Data Exploration
- **Understanding the Data**: Understand the data set, identify problems, and plan next steps.
- **Analyzing Rows**: Use `head()` and `tail()` for initial and final rows (default 5 rows).
- **`df.info()`**: Summarizes the data set, including number of rows/columns, memory usage, data types, column names, and non-null values.
- **`df.describe()`**: Prints statistical data (count, mean, std, min, max).
    - **Quartiles**: 25% (First), 50% (Second), 75% (Third).
- **Metadata**:
    - `df.shape`: Number of rows and columns.
    - `df.columns`: Names of columns.

## Data Manipulation
- **Selection**:
    - Single Column: `column = df["ColumnName"]`.
    - Multiple Columns: `subset = df[["Column1", "Column2", ...]]`.
- **Filtering Rows**:
    - Single Condition: `filter_rows = df[df["Salary"] > 50000]`.
    - Multiple Conditions: `filter_rows = df[(df["Salary"] > 50000) & (df["Column2"] < 80000)]`.
    - Use `|` for the 'or' condition.
- **Adding/Modifying**:
    - Add Column: `df["Bonus"] = df["Salary"] * 0.1`.
    - Insert Method: `df.insert(location, "ColumnName", somedata)`.
    - Modify Value: `df.loc[Row_index, 'ColumnName'] = NewValue`.
- **Removing**:
    - Drop Columns: `df.drop(columns=["ColName"], inplace=True)`.

## Handling Missing Data
- **Types**: `NaN` (Not a Number, for object types), `None`.
- **Checking**:
    - `isnull()`: Returns Boolean (True if missing).
    - Count missing: `df.isnull().sum()`.
- **Fixing**:
    - Remove: `df.dropna(axis=0, inplace=True)` (axis 0=rows, 1=cols).
    - Fill: `df.fillna(value, inplace=True)`.
    - Fill with Mean: `df['cn'] = df['cn'].fillna(df['cn'].mean(), inplace=True)`.
    - Interpolation: `df['cn'] = df['cn'].interpolate(method='linear')`. Useful for time series and trends.

## Sorting, Grouping, and Merging
- **Sorting**: `df.sort_values(by="cn", ascending=True/False, inplace=True)`. Pass a list for multiple columns.
- **Aggregation**: `mean()`, `min()`, `max()`, `sum()`, `count()`, `std()`.
- **Grouping**:
    - `obj = df.groupby('cn1')['cn2'].sum()`.
    - Groups based on unique column values. Pass list for multiple columns.
- **Merging**: `pd.merge(df1, df2, on='cn', how='...')`.
    - Joins: `inner`, `outer`, `left`, `right`.
- **Concatenation**: `pd.concat([df1, df2], axis=0, ignore_index=True)`.
    - `axis=0` (vertical), `axis=1` (horizontal).
- **Cross Join**: Cartesian product (m * n rows).
