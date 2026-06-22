# Numpy Notes

## Introduction
- **Numpy**: Used for handling large datasets efficiently. Handles large data and performs calculations in milliseconds, unlike Python loops .
- **Arrays**: Organized collection of numbers/values 
    - **1d array**: Like a row 
    - **2d array**: Like a table 
    - **3d array**: Stackin

## Creating Arrays
- **From Lists**: `np.array([1, 2, 3, 4])` 
- **Default Values**: `np.zeros(3)`, `np.ones()` 
- **Specific Shape**: `np.full(shape, value)` 
- **Sequences**: `numpy.arange(start, stop, step)` .
- **Identity Matrices**: `np.eye(size)`.

## Attributes & Data Types
- **Attributes**: `shape` (rows, cols) , `size` (total elements), `ndim` (dimensions), `d-type` (data type) .
- **Conversion**: Use `astype()` (e.g., `arr.astype(int)`) .

## Operations
- **Mathematical**: Supports vectorized operations (`+`, `*`, `**`) .
- **Aggregation**: `np.sum()`, `np.mean()`, `np.min()`, `np.max()`, `np.std()`, `np.var()` 

## Indexing & Slicing
- **Indexing**: `array[index]` (1d), `array[row, col]` (2d) . Supports Zero-indexing and Negative indexing .
- **Slicing**: `arr[start:stop:step]` 
- **Advanced**:
    - **Fancy Indexing**: Select list of indices 
    - **Boolean Masking**: Condition-based filtering 
    - **Reversing**: `[::-1]` 

## Reshaping & Modification
- **Reshaping**: `reshape(rows, cols)` (creates a view)
- **Flattening**: `ravel()` (affects original), `flatten()` (returns a copy) 
- **Inserting**: `np.insert(array, index, value, axis)
- **Appending**: `np.append(array, values)` 
- **Stacking**: `vstack()` (row-wise), `hstack()` (column-wise)
- **Splitting**: `split()`, `hsplit()`, `vsplit

## Broadcasting & Missing Values
- **Broadcasting**: Numpy's way of performing operations on different sh.
- **Vectorization**: Mathematical operations on entire arrays at once (alternative to loops).
- **Missing Data**:
    - `np.isnan()`: Detect miss
    - `np.nan_to_num()`: Replace NaN values.
    - `np.isinf()`: Detect infinite values (`posinf`, `neginf`) 
