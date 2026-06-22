# Pandas — Python Data Analysis Library

## What is Pandas?

| Concept | Description |
|---|---|
| **Data Manipulation** | Changing, organizing, or preparing raw data to make it useful and easier to understand |
| **Data Analysis** | Extracting patterns, trends, and insights from data to solve problems |

---

## Core Data Structures

### Series
A **one-dimensional** labeled array that can hold any data type (integers, floats, strings, Python objects). Each element has a unique label called an **index**.

> Best used for tracking changes or patterns over time (e.g., daily sales, temperatures).

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
```

### DataFrame
A **two-dimensional** labeled data structure — like a table in a database, Excel spreadsheet, or SQL table.

- **Rows** → identified by an index (labels)
- **Columns** → identified by column names (labels)

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Salary': [50000, 60000]
})
```

---

## Reading & Writing Files

### Encoding
Encoding converts text into a format computers can store and read.

```python
df = pd.read_csv("sales_data.csv", encoding='latin1')
# Use 'utf-8' or 'latin1' if the file has special characters
# No encoding argument needed if the file reads fine without it
```

### Reading Files

```python
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")
df = pd.read_json("file.json")
```

> **Note:** The file should be in the same directory as your code, or provide the full path.  
> For cloud data (e.g., Google Cloud), use the relevant library such as `gcsfs`.

### Saving Files

```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx")
df.to_json("output.json")
```

---

## Data Exploration

Understanding your dataset before working on it.

```python
df.head()        # First 5 rows (default)
df.tail()        # Last 5 rows (default)
df.head(10)      # First 10 rows
```

```python
df.info()        # Summary: row/column count, data types, non-null values, memory usage
df.describe()    # Statistics: count, mean, std, min, max, quartiles
```

### `df.describe()` Output Explained

| Stat | Description |
|---|---|
| **count** | Number of non-null values |
| **mean** | Average value |
| **std** | Standard deviation |
| **min / max** | Smallest / largest value |
| **25%** | First quartile |
| **50%** | Second quartile (median) |
| **75%** | Third quartile |

```python
df.shape      # (rows, columns)
df.columns    # List of column names
```

---

## Data Selection & Filtering

### Selecting Columns

```python
df["ColumnName"]                       # Single column → returns a Series
df[["Column1", "Column2"]]             # Multiple columns → returns a DataFrame
```

### Filtering Rows

```python
# Single condition
df[df["Salary"] > 50000]

# Multiple conditions — use & (and) / | (or)
df[(df["Salary"] > 50000) & (df["Age"] < 40)]
df[(df["Dept"] == "HR") | (df["Dept"] == "IT")]
```

---

## Adding, Modifying & Removing Data

### Adding Columns

```python
df["Bonus"] = df["Salary"] * 0.1                        # Derive from existing column
df.insert(location, "NewColumn", data)                  # Insert at a specific position
```

### Modifying Values

```python
df.loc[row_index, 'ColumnName'] = new_value             # Modify a specific cell
```

### Removing Columns

```python
df.drop(columns=["ColName"], inplace=True)              # Drop one or more columns
df.drop(index=[0, 1], inplace=True)                     # Drop rows by index
```

---

## Handling Missing Data

### Types of Missing Values

| Type | Used For |
|---|---|
| `NaN` | Numeric / object columns |
| `None` | General Python objects |

### Detecting Missing Values

```python
df.isnull()            # Returns a boolean DataFrame (True = missing)
df.isnull().sum()      # Count of missing values per column
```

### Fixing Missing Values

```python
# Remove rows or columns with missing values
df.dropna(axis=0, inplace=True)     # Drop rows (axis=0)
df.dropna(axis=1, inplace=True)     # Drop columns (axis=1)

# Fill with a fixed value
df.fillna(0, inplace=True)

# Fill with the column mean
df['col'] = df['col'].fillna(df['col'].mean())

# Interpolation (useful for time series / trends)
df['col'] = df['col'].interpolate(method='linear')
```

---

## Sorting, Grouping & Merging

### Sorting

```python
df.sort_values(by="Salary", ascending=True, inplace=True)

# Sort by multiple columns
df.sort_values(by=["Dept", "Salary"], ascending=[True, False], inplace=True)
```

### Aggregation Functions

```python
df["Salary"].mean()    # Average
df["Salary"].sum()     # Total
df["Salary"].min()     # Minimum
df["Salary"].max()     # Maximum
df["Salary"].count()   # Non-null count
df["Salary"].std()     # Standard deviation
```

### Grouping

```python
# Group by one column and aggregate another
df.groupby("Dept")["Salary"].sum()

# Group by multiple columns
df.groupby(["Dept", "City"])["Salary"].mean()
```

> Groups rows with the same unique value in the specified column(s).

### Merging (SQL-style Joins)

```python
pd.merge(df1, df2, on='ColumnName', how='inner')
```

| Join Type | Description |
|---|---|
| `inner` | Only matching rows from both DataFrames |
| `outer` | All rows from both; fills NaN where no match |
| `left` | All rows from left DataFrame |
| `right` | All rows from right DataFrame |

### Concatenation

```python
pd.concat([df1, df2], axis=0, ignore_index=True)   # Stack vertically (rows)
pd.concat([df1, df2], axis=1)                       # Stack horizontally (columns)
```

### Cross Join

```python
pd.merge(df1, df2, how='cross')    # Cartesian product — every row paired with every other row (m × n rows)
```
