# Matplotlib — Python Data Visualization Library

## What is Data Visualization?

Converting data (text, Excel, CSV) into colorful, meaningful, and clear pictures is called **data visualization**.

**Benefits:**
- Analyze trends in data visually
- Saves time
- Easy communication
- Handles big data
- Enables better decision-making
- Integrates with **Pandas** and **NumPy** for data analysis
- Minimizes errors

**Popular Python libraries for data visualization:** Matplotlib, Seaborn, Plotly

---

## Importing Matplotlib

```python
import matplotlib.pyplot as plt
```
`pyplot` provides built-in functions for creating different types of plots.

---

## Plotting a Simple Line Graph

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y)   # plots a line joining the points
plt.show()       # must be called to display the output
```

---

## Key Terms

| Term | Description |
|---|---|
| **Data Point** | A pair of values in the form `(x, y)` |
| **X / Y Axis** | The coordinate axes |
| **Figure** | The canvas for plotting graphs (can hold multiple plots) |
| **Axes** | The area where a single plot is drawn |
| **Plot** | The final result — a set of points representing the data |
| **Marker** | A symbol/dot that makes each data point visible |
| **Line** | Connection between two data points |
| **Line Style** | The style in which two points are joined |
| **Color** | Defines the color of each element (bar, line, etc.) |
| **Legend** | A small box describing what each color represents |
| **Label** | Label for the X and Y axes |
| **Title** | The headline of the graph |
| **Grid** | Horizontal and vertical lines behind the plot |
| **Function** | A block of code that performs a specific task |
| **Method** | A function belonging to an object (OOP concept) |
| **Parameters** | Information passed to functions |
| **Keyword Arguments (kwargs)** | Passed as `name=value` pairs to configure functions |
| **DPI (Dots Per Inch)** | Controls image clarity — higher DPI = higher quality |
| **Object-Oriented API** | Advanced way of creating and managing plots |
| **Backend** | The system Matplotlib uses to render/display graphs |

---

## Common `pyplot` Functions

```python
plt.plot(x, y)         # Plot a line graph
plt.show()             # Display the graph
plt.title('xyz')       # Set the graph title
plt.xlabel('xyz')      # Label the X axis
plt.ylabel('xyz')      # Label the Y axis
plt.legend(loc='upper left', fontsize=value)   # Show legend (requires label= to be set)
plt.grid(color, linestyle, linewidth)          # Add a grid behind the graph
plt.xlim(start, end)   # Set X axis limits
plt.ylim(start, end)   # Set Y axis limits
plt.xticks(old, new)   # Rename/reposition X axis ticks (pass as lists)
plt.yticks(old, new)   # Rename/reposition Y axis ticks (pass as lists)
```

### Full `plt.plot()` with Parameters

```python
plt.plot(x, y,
    color='color name',
    linestyle='linestyle',
    linewidth=value,
    marker='marker symbol',
    label='label name'
)
```

> **Note:** When using `pyplot`, all graphs share the same global canvas. For large datasets with multiple plots, use the **Object-Oriented API** to manage each graph independently.

---

## Types of Charts

### 1. Bar Graph
> Best for **comparing** values across categories.

```python
plt.bar(product, sales, color='color name', label='label name')
```

### 2. Pie Chart
> Best for showing **proportions** within a total distribution.

```python
plt.pie(values, labels=labels_list, autopct='%1.1f%%', colors=color_list)
```
- `autopct` — auto-calculates and displays the percentage for each slice (`%1.1f%%` → 1 decimal place + `%` symbol)

### 3. Histogram
> Best for displaying the **distribution** of continuous data divided into ranges (bins). Bar height = frequency of data in that range.

```python
plt.hist(data, bins=no_of_bins, color='color name', edgecolor='color name')
```

### 4. Scatter Plot
> Best for finding **trends or relationships** between two variables.

```python
plt.scatter(x, y, color='color name', marker='marker style', label='label name')
```

---

## Subplots

Subplots let you draw **multiple plots on the same canvas**.

**Uses:**
- Comparing multiple charts side by side
- Space management
- Quickly analyzing related datasets

### Using `plt.subplot()`

```python
plt.subplot(nrows, ncols, index)
```

**Example:**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.subplot(1, 2, 1)   # 1 row, 2 columns, 1st subplot
plt.plot(x, y)
plt.title('Line Chart')

plt.subplot(1, 2, 2)   # 1 row, 2 columns, 2nd subplot
plt.bar(x, y)
plt.title('Bar Chart')

plt.tight_layout()     # Adjusts spacing between subplots
plt.show()
```

### Using `plt.subplots()` (Object-Oriented API)

```python
fig, ax = plt.subplots(nrows, ncols, figsize=(width, height))
```

```python
fig.suptitle('title')    # Sets a title for the entire figure/canvas
plt.tight_layout()       # Auto-fixes layout (must be called before plt.show())
```

---

## Saving Figures

Save plots as image or document files for easy sharing.

```python
plt.savefig('filename.extension', dpi=value, bbox_inches='tight')
```

| Parameter | Description |
|---|---|
| `extension` | `png`, `jpg`, `svg`, `pdf`, etc. |
| `dpi` | Dots per inch — higher = better resolution |
| `bbox_inches='tight'` | Crops extra white space so the graph fits perfectly |

**Example:**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, color='blue', marker='o')
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Save to current directory
plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')

# Save to a specific folder
# plt.savefig('foldername/line_plot.png', dpi=300, bbox_inches='tight')

plt.show()
```
