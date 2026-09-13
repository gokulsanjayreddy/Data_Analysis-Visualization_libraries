# Seaborn — Statistical Data Visualization in Python

## What is Seaborn?

**Seaborn** is a high-level data visualization library built on top of **Matplotlib** and tightly integrated with **Pandas** data structures. It provides an intuitive API for creating aesthetically pleasing, informative statistical graphics with minimal code.

| Feature | Matplotlib | Seaborn |
|---|---|---|
| **Level of Abstraction** | Low-level (fine control over every pixel) | High-level (automated complex statistical plots) |
| **Data Compatibility** | Works best with NumPy arrays and lists | Designed natively for Pandas DataFrames |
| **Statistical Computations** | Requires manual calculation (e.g. CI, aggregation) | Automatically calculates aggregation, error bars, KDE |
| **Default Aesthetics** | Basic, plain defaults | Modern palettes, grid styles, and clean typography |
| **Syntax** | Verbose (multiple lines for complex figures) | Compact (single function call with hue, col, row) |

---

## Setting Themes and Aesthetics

Seaborn allows you to customize the global appearance of your plots easily.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Set aesthetic theme
sns.set_theme(style="darkgrid", palette="muted")
# Available styles: "white", "dark", "whitegrid", "darkgrid", "ticks"

# Remove top and right spines
sns.despine(top=True, right=True)

# Context scaling: "paper", "notebook", "talk", "poster"
sns.set_context("talk")
```

---

## Summary of Plot Types

| Plot Function | Category | Primary Job | Key Use Case |
|---|---|---|---|
| `sns.scatterplot()` | Relational | Relationship between two numerical variables | Correlation, cluster discovery, multi-group trends |
| `sns.stripplot()` | Categorical Scatter | Categorical variable vs continuous variable | Small datasets, raw data point spread |
| `sns.swarmplot()` | Categorical Scatter | Non-overlapping points showing distribution | Medium datasets, density and frequency without binning |
| `sns.boxplot()` | Distribution / Categorical | Five-number summary (IQR, median, whiskers) | Outlier detection, comparing spread across categories |
| `sns.violinplot()` | Distribution / Categorical | Combines box plot with kernel density estimation | Multimodal distributions, probability density shapes |
| `sns.barplot()` | Categorical / Estimate | Mean (or other metric) with confidence interval | Group comparisons with statistical error estimation |
| `sns.countplot()` | Categorical / Count | Frequency count of categorical occurrences | Bar chart of discrete frequencies (histogram for categories) |
| `sns.heatmap()` | Matrix | 2D color-encoded grid of values | Correlation matrices, confusion matrices, pivot tables |
| `sns.clustermap()` | Matrix / Hierarchy | Hierarchical clustering dendrograms and heatmap | Finding clusters and similarity patterns in multi-feature data |
| `sns.jointplot()` | Bivariate + Univariate | Bivariate relationship with marginal distributions | Joint probability, bivariate scatter/hex/kde with histograms |
| `sns.pairplot()` | Multi-variate Matrix | Pairwise scatterplots across all numerical columns | Rapid exploratory analysis (EDA), feature interaction overview |
| `sns.histplot()` / `kdeplot()` | Distribution | Univariate distribution, frequency, and density | Checking normality, skewness, spread of single variables |

---

## 1. Scatter Plot (`sns.scatterplot`)

Plots data points on a 2D Cartesian plane to show the correlation or relationship between two continuous features.

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='sex',          # Color by category
    style='smoker',     # Different marker shapes
    size='size',        # Point sizes scaled by a numerical column
    sizes=(20, 200),    # Min and max marker sizes
    palette='Set2',     # Color palette
    alpha=0.8           # Transparency
)
plt.title('Total Bill vs Tip by Gender and Smoker Status')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()
```

### Key Parameters:
- `data`: DataFrame name.
- `x`, `y`: Column names for axes.
- `hue`: Grouping variable that assigns different colors.
- `style`: Grouping variable that assigns different marker shapes (`o`, `s`, `^`, etc.).
- `size`: Grouping variable that scales marker area.
- `palette`: Color scheme (e.g. `'viridis'`, `'deep'`, `'coolwarm'`).

---

## 2. Categorical Scatter Plots: Strip Plot and Swarm Plot

Used when one variable is categorical and the other is numerical.

### Strip Plot (`sns.stripplot`)
Draws a scatter plot where one axis is categorical. Uses `jitter` to add random noise to prevent dots from completely overlapping.

```python
# Strip Plot with Jitter
plt.figure(figsize=(8, 5))
sns.stripplot(
    data=tips,
    x='day',
    y='total_bill',
    jitter=0.2,       # Spreads overlapping points horizontally
    hue='sex',
    dodge=True,       # Separates hue groups side by side
    palette='Accent'
)
plt.title('Bill Distribution per Day (Strip Plot)')
plt.show()
```

### Swarm Plot (`sns.swarmplot`)
Positions points using an algorithm that prevents any overlap, resembling a "beeswarm" shape that visualizes distribution density.

```python
# Swarm Plot
plt.figure(figsize=(8, 5))
sns.swarmplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='sex',
    dodge=True,
    palette='muted',
    size=6
)
plt.title('Bill Distribution per Day (Swarm Plot)')
plt.show()
```

> **Tip:** Swarm plots scale poorly with very large datasets ($N > 1000$). For large datasets, prefer `boxplot`, `violinplot`, or `stripplot`.

---

## 3. Box Plot (`sns.boxplot`)

Depicts the distribution of numerical data through quartiles. Excellent for spotting **skewness** and **outliers**.

```
    Outlier        Q1 (25th)     Median (50th)    Q3 (75th)          Outlier
       o     |--------[==============|==============]--------|           o
             Min           <------- IQR ------->            Max
```

```python
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='smoker',
    palette='pastel',
    width=0.6,
    fliersize=5      # Size of marker used to indicate outliers
)
plt.title('Bill Distribution by Day and Smoking Status')
plt.show()
```

### Understanding the 5 Numbers:
1. **Median (Q2 / 50th percentile)**: Center line inside the box.
2. **Q1 (25th percentile)**: Left/bottom boundary of the box.
3. **Q3 (75th percentile)**: Right/top boundary of the box.
4. **IQR (Interquartile Range)**: $IQR = Q3 - Q1$.
5. **Whiskers**: Extend to $1.5 \times IQR$ beyond Q1 and Q3. Data points beyond whiskers are plotted as individual outlier points.

---

## 4. Violin Plot (`sns.violinplot`)

Combines the box plot with a **Kernel Density Estimate (KDE)** on both sides. Reveals multiple peaks (multimodal data) that box plots conceal.

```python
plt.figure(figsize=(8, 5))
sns.violinplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='sex',
    split=True,       # Fuses male and female into left/right halves of one violin
    inner='quart',    # Shows dashed lines for quartiles inside
    palette='coolwarm'
)
plt.title('Total Bill Violin Plot with Split Hue')
plt.show()
```

### Key Parameters:
- `split=True`: When `hue` has exactly 2 levels, draws half of the violin for each level.
- `inner`: `'box'` (mini box plot), `'quart'` (quartiles), `'point'` (scatter points), or `None`.

---

## 5. Bar Plot and Count Plot

### Bar Plot (`sns.barplot`)
Calculates an aggregate estimate (default: **mean**) of a numerical variable across categories, with error bars representing the confidence interval (CI).

```python
import numpy as np

plt.figure(figsize=(8, 5))
sns.barplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='sex',
    estimator=np.mean,    # Can also be np.median, np.sum, np.std
    errorbar='ci',        # Error bar style (ci, se, sd, or None)
    palette='Blues'
)
plt.title('Average Total Bill per Day with Error Bars')
plt.show()
```

### Count Plot (`sns.countplot`)
A specialized bar plot that simply counts the number of occurrences of each category (equivalent to `df['col'].value_counts()`).

```python
plt.figure(figsize=(7, 4))
sns.countplot(
    data=tips,
    x='day',
    hue='time',
    palette='dark'
)
plt.title('Customer Visit Counts by Day and Meal Time')
plt.show()
```

---

## 6. Heatmap (`sns.heatmap`)

Visualizes 2D numerical matrices as a grid of colored cells. Most frequently used for **correlation matrices** and **pivot tables**.

```python
# Correlation matrix
numeric_df = tips.select_dtypes(include='number')
corr = numeric_df.corr()

plt.figure(figsize=(7, 5))
sns.heatmap(
    corr,
    annot=True,          # Write values inside cells
    fmt=".2f",           # Float format
    cmap='coolwarm',     # Color palette
    vmin=-1, vmax=1,     # Fix color range limits
    linewidths=0.5,      # Grid line borders between cells
    cbar=True            # Show colorbar legend
)
plt.title('Correlation Matrix of Tips Dataset')
plt.show()
```

### Pivot Table Heatmap:
```python
flights = sns.load_dataset('flights')
flight_matrix = flights.pivot(index='month', columns='year', values='passengers')

plt.figure(figsize=(10, 6))
sns.heatmap(flight_matrix, cmap='YlGnBu', fmt='d', annot=True)
plt.title('Monthly Flight Passengers (1949 - 1960)')
plt.show()
```

---

## 7. Clustermap (`sns.clustermap`)

Performs **hierarchical agglomerative clustering** on rows and columns of a 2D matrix and arranges similar rows/columns adjacent to each other, accompanied by dendrograms.

```python
# Clustermap of flight passenger data
sns.clustermap(
    flight_matrix,
    cmap='viridis',
    standard_scale=1,    # Standardize data across columns (0 to 1 scale)
    metric='euclidean',  # Distance metric
    method='ward',       # Linkage method
    figsize=(9, 8)
)
plt.show()
```

> **Note:** `sns.clustermap` creates its own `Figure` using `ClusterGrid`. Do not wrap it in `plt.figure()`.

---

## 8. Joint Plot (`sns.jointplot`)

Plots a bivariate relationship in the center with two univariate marginal plots (histograms or KDEs) on the top and right margins.

```python
# Scatter with histograms
sns.jointplot(
    data=tips,
    x='total_bill',
    y='tip',
    kind='scatter',    # Options: 'scatter', 'hex', 'kde', 'reg', 'resid'
    hue='sex',
    palette='Set1'
)
plt.show()

# Hexagonal binning (ideal for dense overlapping points)
sns.jointplot(
    data=tips,
    x='total_bill',
    y='tip',
    kind='hex',
    color='purple'
)
plt.show()
```

---

## 9. Pair Plot (`sns.pairplot`)

Constructs a grid of subplots visualizing pairwise relationships between all numerical features in a DataFrame.

```python
# Comprehensive Pairplot on Iris
iris = sns.load_dataset('iris')

sns.pairplot(
    iris,
    hue='species',
    palette='husl',
    diag_kind='kde',    # 'kde' or 'hist' on diagonal
    corner=True,        # Show only lower triangle to eliminate duplicate comparisons
    markers=['o', 's', 'D']
)
plt.show()
```

### Key Parameters:
- `diag_kind='kde'`: Draws smooth density curves along the diagonal.
- `corner=True`: Omits redundant mirror plots above the diagonal.
- `vars=['total_bill', 'tip']`: Subsets specific columns rather than all numeric fields.

---

## 10. Distribution Plots: Histplot, KDE and Distplot

### Univariate Histograms and KDE (`sns.histplot`)
`sns.histplot` is the modern, feature-rich replacement for the legacy `sns.distplot`.

```python
plt.figure(figsize=(8, 5))
sns.histplot(
    data=tips,
    x='total_bill',
    kde=True,           # Overlay Kernel Density Estimate curve
    bins=20,            # Number of histogram bins
    hue='sex',          # Group by category
    multiple='stack',   # 'layer', 'dodge', 'stack', 'fill'
    palette='bright'
)
plt.title('Distribution of Total Bill with KDE')
plt.show()
```

### Pure Density Curves (`sns.kdeplot`)
```python
plt.figure(figsize=(8, 5))
sns.kdeplot(
    data=tips,
    x='total_bill',
    hue='time',
    fill=True,          # Fill area under curve
    common_norm=False,  # Normalize each group independently
    palette='magma'
)
plt.title('KDE of Total Bill by Lunch vs Dinner')
plt.show()
```

### Legacy `sns.distplot` (for backwards compatibility):
```python
# Legacy distplot (deprecated in Seaborn 0.11+)
sns.distplot(tips['total_bill'], bins=15, kde=True, rug=True)
plt.show()
```

---

## Quick Rules of Thumb

1. **Continuous vs Continuous:** `sns.scatterplot()`, `sns.jointplot()`, or `sns.pairplot()`.
2. **Categorical vs Continuous:** `sns.boxplot()`, `sns.violinplot()`, or `sns.barplot()`.
3. **Categorical vs Categorical:** `sns.countplot(hue=...)` or pivot table `sns.heatmap()`.
4. **Single Continuous Distribution:** `sns.histplot(kde=True)` or `sns.kdeplot()`.
5. **Correlation and Multivariable Patterns:** `sns.heatmap(df.corr())` or `sns.clustermap()`.
6. **Want clean visuals:** Always call `sns.set_theme()` at the start and `sns.despine()` before `plt.show()`.
