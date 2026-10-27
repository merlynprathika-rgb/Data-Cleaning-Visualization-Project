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
