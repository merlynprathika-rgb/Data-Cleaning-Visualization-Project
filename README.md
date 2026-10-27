Step 1: Install and import libraries
# Install these libraries if needed# !pip install pandas numpy matplotlib seabornimport pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport seaborn as snsprint("Libraries imported successfully!")



Step 2: Create a raw dataset
This example includes missing values, outliers, and duplicate records so you can demonstrate data cleaning.
data = {    "Name": [        "Aman", "Riya", "Karan", "Neha", "Rohit",        "Simran", "Priya", "Arjun", "Karan", "Aman"    ],    "Age": [18, 19, 20, np.nan, 21, 22, 19, 20, 20, 18],    "Study_Hours": [2, 4, 3, 5, np.nan, 6, 4, 3, 3, 2],    "Marks": [65, 85, 72, 90, 88, 95, np.nan, 75, 72, 65],    "Attendance": [75, 90, 80, 95, 88, 98, 85, 82, 80, 75]}df = pd.DataFrame(data)print("RAW DATASET")print(df)print("\nDataset Shape:", df.shape)



Step 3: Explore the dataset
print("Dataset Information:")df.info()print("\nStatistical Summary:")print(df.describe())print("\nMissing Values:")print(df.isnull().sum())print("\nDuplicate Rows:", df.duplicated().sum())



Step 4: Handle missing values
Fill missing numerical values using the median, which is less affected by extreme values than the mean.
numeric_columns = ["Age", "Study_Hours", "Marks", "Attendance"]for column in numeric_columns:    df[column] = df[column].fillna(df[column].median())print("Missing Values After Cleaning:")print(df.isnull().sum())



Step 5: Remove duplicate records
print("Duplicates Before:", df.duplicated().sum())df = df.drop_duplicates().reset_index(drop=True)print("Duplicates After:", df.duplicated().sum())print("\nCleaned Dataset:")print(df)



Step 6: Detect and handle outliers
Use the Interquartile Range (IQR) method to identify unusual numerical values. This example caps outliers at the IQR limits instead of deleting entire rows.
outlier_columns = ["Age", "Study_Hours", "Marks", "Attendance"]for column in outlier_columns:    Q1 = df[column].quantile(0.25)    Q3 = df[column].quantile(0.75)    IQR = Q3 - Q1    lower_limit = Q1 - 1.5 * IQR    upper_limit = Q3 + 1.5 * IQR    outliers = (        (df[column] < lower_limit) |        (df[column] > upper_limit)    )    print(f"{column}: {outliers.sum()} outlier(s) detected")    df[column] = df[column].clip(        lower=lower_limit,        upper=upper_limit    )print("\nOutlier handling completed.")



Note: Outlier treatment should be based on the data and domain knowledge. Capping is used here for demonstration.
Step 7: Create visualizations
A. Marks distribution — Histogram
plt.figure(figsize=(8, 5))plt.hist(df["Marks"], bins=5, edgecolor="black")plt.title("Distribution of Student Marks")plt.xlabel("Marks")plt.ylabel("Number of Students")plt.grid(axis="y", alpha=0.3)plt.show()



B. Study hours vs marks — Scatter plot
plt.figure(figsize=(8, 5))sns.scatterplot(    data=df,    x="Study_Hours",    y="Marks",    s=100)plt.title("Study Hours vs Student Marks")plt.xlabel("Study Hours")plt.ylabel("Marks")plt.show()



C. Correlation heatmap
plt.figure(figsize=(8, 5))correlation = df[    ["Age", "Study_Hours", "Marks", "Attendance"]].corr()sns.heatmap(    correlation,    annot=True,    cmap="coolwarm",    fmt=".2f")plt.title("Correlation Between Student Variables")plt.show()



D. Attendance comparison — Bar chart
plt.figure(figsize=(9, 5))plt.bar(df["Name"], df["Attendance"])plt.title("Student Attendance")plt.xlabel("Student Name")plt.ylabel("Attendance (%)")plt.xticks(rotation=45)plt.tight_layout()plt.show()



E. Marks outliers — Box plot
plt.figure(figsize=(8, 4))sns.boxplot(x=df["Marks"])plt.title("Box Plot of Student Marks")plt.xlabel("Marks")plt.show()



Step 8: Generate a final report
print("===== DATA CLEANING REPORT =====")print("Total Records:", len(df))print("Total Columns:", len(df.columns))print("Missing Values:", df.isnull().sum().sum())print("Duplicate Rows:", df.duplicated().sum())print("\nAverage Marks:", round(df["Marks"].mean(), 2))print("Highest Marks:", df["Marks"].max())print("Lowest Marks:", df["Marks"].min())print("Average Study Hours:", round(df["Study_Hours"].mean(), 2))print("Average Attendance:", round(df["Attendance"].mean(), 2))print("\nTop Performing Student:")print(df.loc[df["Marks"].idxmax(), ["Name", "Marks"]])print("\n===== REPORT COMPLETED =====")



Step 9: Save the cleaned dataset
df.to_csv("cleaned_student_dataset.csv", index=False)print("Cleaned dataset saved successfully!")



In Google Colab, download the file using:
from google.colab import filesfiles.download("cleaned_student_dataset.csv")
