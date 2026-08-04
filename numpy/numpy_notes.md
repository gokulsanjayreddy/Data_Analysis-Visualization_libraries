# NumPy — Numerical Python

## What is NumPy?

**NumPy** is a Python library used for handling large datasets efficiently. Unlike standard Python loops, NumPy performs calculations on large data in milliseconds using optimized, low-level operations.

---

## Creating Arrays

Arrays are organized collections of numbers/values. NumPy supports 1D, 2D, and 3D arrays.

| Dimension | Description | Visual Analogy |
|---|---|---|
| **1D Array** | A single sequence of values | A row |
| **2D Array** | Rows and columns | A table |
| **3D Array** | Multiple stacked tables | A stack of tables |

```python
import numpy as np

# From a list
np.array([1, 2, 3, 4])

# Filled with zeros or ones
np.zeros(3)           # [0. 0. 0.]
np.ones((2, 3))       # 2x3 array of 1s

# Filled with a specific value
np.full((2, 3), 7)    # 2x3 array filled with 7

# A range sequence
np.arange(start, stop, step)

# Identity matrix (diagonal = 1, rest = 0)
np.eye(size)
```

---

## Array Attributes & Data Types

```python
arr.shape    # (rows, cols) — dimensions of the array
arr.size     # Total number of elements
arr.ndim     # Number of dimensions
arr.dtype    # Data type of elements (int32, float64, etc.)
arr.nbytes   # Total memory size of array elements in bytes
arr.itemsize # Memory size of each single element in bytes
```

### Type Conversion

```python
arr.astype(int)     # Convert to integer
arr.astype(float)   # Convert to float
```

---

## Mathematical Operations

NumPy supports **vectorized operations** — applied to the entire array at once, without loops.

```python
arr + 5       # Add 5 to every element
arr * 2       # Multiply every element by 2
arr ** 2      # Square every element
arr1 + arr2   # Element-wise addition of two arrays
```

### Element-wise vs Matrix Multiplication

```python
a * b           # Element-wise multiplication
a.dot(b)        # Matrix dot product / matrix multiplication
np.matmul(a, b) # Matrix multiplication function
```

### Trigonometric & Mathematical Functions

```python
np.sin(arr)     # Calculate sine of elements (in radians)
np.cos(arr)     # Calculate cosine of elements (in radians)
```

### Aggregation Functions

```python
np.sum(arr)    # Total sum
np.mean(arr)   # Average
np.min(arr)    # Minimum value
np.max(arr)    # Maximum value
np.std(arr)    # Standard deviation
np.var(arr)    # Variance
```

### Applying Functions Along Axis

```python
# Apply custom/built-in function along a specific axis (axis=1 for rows, axis=0 for columns)
np.apply_along_axis(lambda x: np.min(x), axis=1, arr=a)
```

---

## Indexing & Slicing

### Basic Indexing

```python
# 1D
arr[0]        # First element (zero-indexed)
arr[-1]       # Last element (negative indexing)

# 2D
arr[row, col]
arr[0, 1]     # First row, second column
```

### Slicing

```python
arr[start:stop:step]

arr[1:4]      # Elements from index 1 to 3
arr[::2]      # Every other element
arr[::-1]     # Reverse the array
```

### Advanced Indexing & Masking

```python
# Fancy Indexing — select specific indices
arr[[0, 2, 4]]

# Boolean Masking — filter by condition
arr[arr > 10]

# Conditional Replacement via Masking
arr[arr < 0] = 6    # Replace negative elements with 6

# Reversing
arr[::-1]           # Reverse 1D array or row order of a 2D array
```

---

## Searching, Selection & Conditionals

```python
# Checking Element Membership
np.isin(a, 5)             # Check if 5 exists in array (returns boolean array)
np.isin(5, a)             # Check if scalar 5 is present in array a

# Boolean Evaluation along Axes
np.any(arr > 40, axis=1)  # Returns True for each row if ANY element in that row > 40
np.all(arr > 40, axis=1)  # Returns True for each row if ALL elements in that row > 40

# Finding Indices
np.where(condition)       # Tuple of index arrays where condition is True
np.where(np.any(a > 40, axis=1))  # Row indices where any element > 40

# Bitwise NOT (~) for Inverting Boolean Masks
# Filter out rows containing NaN values:
a[~np.isnan(a).any(axis=1)]

# Element-wise Comparisons
a == b                    # Element-wise equality check
a > b                     # Element-wise greater than check
a < b                     # Element-wise less than check
```

---

## Reshaping & Modification

### Reshaping

```python
arr.reshape(rows, cols)   # Returns a view (changes reflect on original)
```

### Flattening & Squeezing

```python
arr.ravel()     # Flattens to 1D — affects the original array
arr.flatten()   # Flattens to 1D — returns an independent copy
arr.squeeze()   # Removes single-dimensional entries (dimensions of size 1)
```

### Inserting, Deleting & Overwriting

```python
np.insert(array, index, value, axis)   # Insert value at a specific index along axis
np.delete(array, index, axis)          # Delete row/column at a specific index along axis
np.append(array, values)               # Append values to the end

# Replace/put values at specific flat 1D indices
a.put([1, 2, 3, 4, 0], b)              # Insert/overwrite values of b at specified flat indices

# Diagonal Manipulation
np.fill_diagonal(arr, val)             # Replace main diagonal elements in-place with val
```

### Array Padding (Borders)

```python
# Add border line / padding filled with constant value (e.g. 0) around array
np.pad(arr, pad_width=2, mode='constant', constant_values=0)
```

### Stacking, Splitting & Concatenation

```python
# Stacking
np.vstack([arr1, arr2])    # Stack row-wise (vertical)
np.hstack([arr1, arr2])    # Stack column-wise (horizontal)
np.concatenate((arr1, arr2), axis=0)  # Join arrays along existing axis

# Splitting
np.split(arr, n)            # Split into n equal parts
np.hsplit(arr, n)           # Split horizontally
np.vsplit(arr, n)           # Split vertically
```

---

## Broadcasting

**Broadcasting** is NumPy's way of performing operations on arrays of different shapes without copying data.

```python
arr = np.array([1, 2, 3])
arr + 10   # 10 is broadcast across all elements → [11, 12, 13]
```

> NumPy automatically expands the smaller array to match the shape of the larger one, as long as their dimensions are compatible.

---

## Handling Missing & Infinite Values

```python
np.isnan(arr)             # Detect NaN (missing) values → returns boolean array
np.nan_to_num(arr)        # Replace NaN with 0 (or specify fill values)

np.isinf(arr)             # Detect infinite values (both +inf and -inf)
np.isposinf(arr)          # Detect positive infinity
np.isneginf(arr)          # Detect negative infinity

# Filtering out rows containing NaN values using bitwise NOT ~
clean_arr = arr[~np.isnan(arr).any(axis=1)]
```

---

## String Operations (`np.char`)

NumPy provides vectorized string operations for arrays containing string elements via `np.char`.

```python
import numpy as np

a = np.array(['Hello', 'world', 'python'])

np.char.upper(a)       # Convert string elements to uppercase
np.char.lower(a)       # Convert string elements to lowercase
np.char.capitalize(a)  # Capitalize first letter of each string
np.char.title(a)       # Title case each string
np.char.swapcase(a)    # Swap uppercase to lowercase and vice versa
np.char.multiply(a, 2) # Repeat string elements (e.g. ['HelloHello', 'worldworld', ...])
```
