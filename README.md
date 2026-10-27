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
Run the script:

bash
python data_cleaning_visualization.py
The cleaned dataset will be saved to:

bash
data/cleaned_student_data.csv
Charts will be saved in the outputs/ folder.

Files in This Project
data/raw_student_data.csv — raw dataset with data quality issues
data_cleaning_visualization.py — main data cleaning and visualization pipeline
requirements.txt — Python dependencies
outputs/ — generated charts after execution
Example Insights
After cleaning and analysis, you can typically observe:

students with higher study hours tend to score higher
attendance is positively associated with academic performance
a few extreme values should be treated carefully before modeling
This project is useful for learning practical data preprocessing and exploratory data analysis in Python.

Code
requirements.txt

txt
pandas>=2.0.0
numpy>=1.26.0
matplotlib>=3.7.0
seaborn>=0.13.0

data/raw_student_data.csv

CSV
Name,Age,Gender,Study_Hours,Marks,Attendance,Department
Aman,18,Male,5.0,78,88,Computer Science
Riya,19,Female,6.5,85,92,Information Technology
Karan,20,Male,7.0,80,90,Computer Science
Neha,,Female,4.5,60,85,Information Technology
Rohit,21,Male,8.0,88,95,Mechanical
Simran,22,Female,5.5,72,86,Computer Science
Priya,19,Female,7.5,91,94,Information Technology
Arjun,20,Male,9.0,96,98,Computer Science
Karan,20,Male,7.0,80,90,Computer Science
Aman,18,Male,5.0,78,88,Computer Science
Meera,17,Female,6.0,,89,Electronics
Rahul,23,Male,12.0,65,78,Electronics
Tina,21,Female,4.0,58,75,Computer Science
Vivek,24,Male,3.5,28,68,Information Technology
Sanya,18,Female,8.0,94,97,Electronics
Deepa,19,Female,6.8,75,89,Computer Science
Isha,,Female,7.2,66,83,Information Technology
Yash,25,Male,10.0,100,99,Mechanical

data_cleaning_visualization.py

py
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_dataset():
    raw_path = DATA_DIR / "raw_student_data.csv"
    df = pd.read_csv(raw_path)
    print("Dataset loaded successfully.")
    print(f"Shape: {df.shape}")
    return df


def print_summary(df):
    print("\nDataset Information:")
    df.info()
    print("\nStatistical Summary:")
    print(df.describe(include="all"))
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())


def clean_dataset(df):
    cleaned = df.copy()
    numeric_columns = ["Age", "Study_Hours", "Marks", "Attendance"]

    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    print("\nFilling missing numeric values with median values...")
    for column in numeric_columns:
        median_value = cleaned[column].median()
        cleaned[column] = cleaned[column].fillna(median_value)

    print("\nRemoving duplicate rows...")
    cleaned = cleaned.drop_duplicates().reset_index(drop=True)

    print("\nHandling outliers using the IQR method...")
    for column in numeric_columns:
        q1 = cleaned[column].quantile(0.25)
        q3 = cleaned[column].quantile(0.75)
        iqr = q3 - q1
        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr
        cleaned[column] = cleaned[column].clip(lower_limit, upper_limit)

    return cleaned


def save_cleaned_dataset(df):
    cleaned_path = DATA_DIR / "cleaned_student_data.csv"
    df.to_csv(cleaned_path, index=False)
    print(f"\nCleaned dataset saved to: {cleaned_path}")


def create_visualizations(df):
    plt.figure(figsize=(8, 5))
    plt.hist(df["Marks"], bins=6, edgecolor="black", color="steelblue")
    plt.title("Distribution of Student Marks")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "marks_distribution.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="Study_Hours", y="Marks", s=110, color="darkorange")
    plt.title("Study Hours vs Student Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "study_hours_vs_marks.png")
    plt.close()

    plt.figure(figsize=(8, 6))
    corr = df[["Age", "Study_Hours", "Marks", "Attendance"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "correlation_heatmap.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    sns.barplot(data=df, x="Name", y="Attendance", palette="viridis")
    plt.title("Student Attendance")
    plt.xlabel("Student Name")
    plt.ylabel("Attendance (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "attendance_bar_chart.png")
    plt.close()

    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df["Marks"], color="lightgreen")
    plt.title("Box Plot of Student Marks")
    plt.xlabel("Marks")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "marks_boxplot.png")
    plt.close()

    print(f"\nVisualization files saved to: {OUTPUT_DIR}")


def main():
    raw_df = load_dataset()
    print_summary(raw_df)
    cleaned_df = clean_dataset(raw_df)
    print("\nCleaned Data Preview:")
    print(cleaned_df.head(15))
    save_cleaned_dataset(cleaned_df)
    create_visualizations(cleaned_df)
    print("\nData cleaning and visualization project completed successfully.")


if __name__ == "__main__":
    main()
