# 📊 Data Analysis & Visualization Libraries

> A structured collection of practice notebooks, study notes, and code experiments covering core Python data science libraries.

---

## 🗂️ Repository Structure

```
Data_Analysis-Visualization_libraries/
│
├── Pandas/                     # Data manipulation & cleaning workflows
│   ├── pandas_notes.md         # Concept notes and quick reference
│   └── examples.py             # Practical code examples
│
├── numpy/                      # Numerical computing & array operations
│   ├── numpy_notes.md
│   └── examples.py
│
├── mplib/                      # Data visualization with Matplotlib
│   ├── matplotlib_notes.md
│   └── examples.py
│
├── seaborn/                    # Statistical data visualization with Seaborn
│   ├── seaborn_notes.md        # Concept notes and quick reference
│   ├── datasets/               # Practice datasets (tips, flights, titanic)
│   ├── scatterplot.ipynb       # 2D continuous relationships & styling
│   ├── stripplot_and_swarmplot.ipynb # Categorical scatter plots (jitter & beeswarm)
│   ├── boxplot.ipynb           # Five-number summary & outlier detection
│   ├── violinplot.ipynb        # Kernel density + boxplot distributions
│   ├── barplot_and_countplot.ipynb # Statistical estimates & frequency counts
│   ├── heatmap.ipynb           # 2D correlation & pivot matrix plots
│   ├── clustermap.ipynb        # Hierarchical clustering dendrograms
│   ├── jointplot.ipynb         # Bivariate & marginal distributions
│   ├── pairplot.ipynb          # Multi-variate pairwise relationship grids
│   └── distplot.ipynb          # Univariate histograms, KDE curves & rug plots
│   
└── README.md
```

> **Note:** Most examples are written as Jupyter Notebooks (`.ipynb`) for interactive exploration.

---

## 📚 Libraries Covered

### 🐼 Pandas
Covers the full data manipulation lifecycle — from loading raw data to cleaning, transforming, and aggregating.

**Key topics:**
- DataFrame and Series operations
- Data cleaning and handling missing values
- GroupBy, merge, join, and reshape
- Time-series analysis
- Reading/writing CSV, Excel, and JSON

### 🔢 NumPy
Focuses on high-performance numerical operations that form the backbone of data science in Python.

**Key topics:**
- ndarray creation and manipulation
- Vectorized operations and broadcasting
- Linear algebra and mathematical functions
- Indexing, slicing, and fancy indexing
- Random number generation

### 📈 Matplotlib (`mplib`)
Covers creating clear, customizable visualizations from raw data.

**Key topics:**
- Line, bar, scatter, and histogram plots
- Subplots and figure layouts
- Axis customization (labels, ticks, legends)
- Saving and exporting figures
- Combining with Pandas/NumPy for end-to-end plotting

### Seaborn (`seaborn`)
Covers statistical data visualization built on top of Matplotlib and tightly integrated with Pandas DataFrames (based on CampusX playlist curriculum).

**Key topics:**
- Relational plots (Scatter plots with hue, style, and size)
- Categorical scatter plots (Stripplots with jitter and Swarmplots)
- Distribution plots across categories (Boxplots, IQR analysis, and Violinplots)
- Statistical aggregation plots (Barplots with confidence intervals and Countplots)
- Matrix plots (Correlation heatmaps, pivot tables, and hierarchical clustermaps)
- Multi-variable relationship plots (Jointplots and pairwise Pairplots)
- Univariate distribution plots (Histplots, KDE density curves, and rug plots)

---

## ⚙️ Prerequisites & Setup

Make sure you have **Python 3.8+** installed. Then install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Clone the Repository

```bash
git clone https://github.com/gokulsanjayreddy/Data_Analysis-Visualization_libraries.git
cd Data_Analysis-Visualization_libraries
```

### Run Jupyter Notebooks

```bash
jupyter notebook
```

Then open any `.ipynb` file from within the browser interface.

---

## 🚀 How to Use This Repo

- Browse each library folder to find notes and working code examples.
- The `.md` files serve as quick-reference guides.
- The `.ipynb` / `.py` files contain runnable code you can experiment with directly.
- Start with `Pandas` → `NumPy` → `Matplotlib` if you're learning from scratch.

---

## 🤝 Contributions

This is a personal learning repository, but feedback and suggestions are welcome!

- Found a bug or a better approach? Open an **Issue**.
- Want to contribute an example or improvement? Submit a **Pull Request**.

---

*Visit  @[profile](https://github.com/gokulsanjayreddy)*

---
