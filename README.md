# Data Cleaning & Visualization Project

This project demonstrates a full data cleaning workflow on a raw student performance dataset. It covers missing value treatment, duplicate removal, outlier handling, and data storytelling through visualizations.

## Objective

The goal is to transform a raw dataset into a clean dataset that can be used for analysis and reporting. The project focuses on:

- Handling missing values
- Removing duplicate records
- Detecting and capping outliers
- Creating visual summaries using Python
- Saving the cleaned data for further analysis

## Dataset

The project uses a raw student dataset stored in:

- `data/raw_student_data.csv`

The dataset contains columns such as:

- `Name`
- `Age`
- `Gender`
- `Study_Hours`
- `Marks`
- `Attendance`
- `Department`

It intentionally includes:

- missing values
- duplicate rows
- outlier values

## Workflow

The script `data_cleaning_visualization.py` performs the following steps:

1. Load the raw dataset
2. Inspect row count, data types, and missing values
3. Fill numerical missing values using median values
4. Drop duplicate records
5. Detect outliers using the IQR method
6. Cap outliers to the valid range
7. Generate summary charts
8. Save the cleaned dataset and visuals

## Visualizations Created

The script produces the following charts:

- Distribution of student marks
- Study hours vs marks scatter plot
- Correlation heatmap
- Attendance by student bar chart
- Box plot of marks

## How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:

   ```bash
   python data_cleaning_visualization.py
   ```

3. The cleaned dataset will be saved to:

   ```bash
   data/cleaned_student_data.csv
   ```

4. Charts will be saved in the `outputs/` folder.

## Files in This Project

- `data/raw_student_data.csv` — raw dataset with data quality issues
- `data_cleaning_visualization.py` — main data cleaning and visualization pipeline
- `requirements.txt` — Python dependencies
- `outputs/` — generated charts after execution

## Example Insights

After cleaning and analysis, you can typically observe:

- students with higher study hours tend to score higher
- attendance is positively associated with academic performance
- a few extreme values should be treated carefully before modeling

This project is useful for learning practical data preprocessing and exploratory data analysis in Python.
