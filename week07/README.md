# Week 07 — Data Visualization Lab

## Overview
This lab focuses on data validation, exploratory data visualization, and building a multi-panel dashboard using Matplotlib and Pandas.

---

## Structure & Deliverables
- `visualization_lab.ipynb`: Complete notebook containing all analysis, charts, and interpretations.
- `figures/`: Exported figures including individual plots and final dashboard files:
  - `b1_weekly_attendance_trend.png`
  - `b2_attendance_vs_final.png`
  - `c1_weighted_score_histogram.png`
  - `c2_weighted_score_boxplot.png`
  - `c3_program_average_scores.png`
  - `student_dashboard.png` (300 DPI)
  - `student_dashboard.pdf` (Vector format)

---

## Key Tasks Completed

### 1. Part A — Setup and Data Validation
- Prepared output directory `figures/`.
- Loaded cleaned dataset `students_clean.csv` from Week 06.
- Verified schema for required columns: `program`, `attendance`, `final`, `weighted_score`, `grade`.
- Confirmed zero missing values across target fields and validated that all scores lie within the range of 0 to 100.

### 2. Part B — Trend and Relationship Charts
- **Line Plot (B1):** Visualized weekly attendance trend over 6 weeks.
- **Scatter Plot (B2):** Evaluated relationship between attendance and final exam scores.

### 3. Part C — Distributions and Comparisons
- **Histogram (C1):** Plotted distribution of weighted scores using 10 bins.
- **Box Plot (C2):** Generated horizontal box plot showing median and spread.
- **Bar Chart (C3):** Compared average weighted scores across academic programs.

### 4. Part D — Student Performance Dashboard
- Assembled a $2 \times 2$ unified dashboard combining the histogram, scatter plot, bar chart, and box plot.
- Exported reproducible files in both high-resolution PNG (300 DPI) and PDF formats.

---

## Execution
Run the Jupyter Notebook:
```bash
uv run jupyter notebook week07/visualization_lab.ipynb