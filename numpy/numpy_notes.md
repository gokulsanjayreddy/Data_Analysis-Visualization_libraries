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

### Aggregation Functions

```python
np.sum(arr)    # Total sum
np.mean(arr)   # Average
np.min(arr)    # Minimum value
np.max(arr)    # Maximum value
np.std(arr)    # Standard deviation
np.var(arr)    # Variance
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

### Advanced Indexing

```python
# Fancy Indexing — select specific indices
arr[[0, 2, 4]]

# Boolean Masking — filter by condition
arr[arr > 10]

# Reversing
arr[::-1]
```

---

## Reshaping & Modification

### Reshaping

```python
arr.reshape(rows, cols)   # Returns a view (changes reflect on original)
```

### Flattening

```python
arr.ravel()     # Flattens to 1D — affects the original array
arr.flatten()   # Flattens to 1D — returns an independent copy
```

### Inserting & Appending

```python
np.insert(array, index, value, axis)   # Insert value at a specific index
np.append(array, values)               # Append values to the end
```

### Stacking & Splitting

```python
# Stacking
np.vstack([arr1, arr2])    # Stack row-wise (vertical)
np.hstack([arr1, arr2])    # Stack column-wise (horizontal)

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
```
