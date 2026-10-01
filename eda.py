import pandas as pd

# Load dataset
df = pd.read_csv("data/student_performance.csv")

print("========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

print("\n========== CORRELATION WITH FINAL SCORE ==========")
correlation = df.corr(numeric_only=True)["final_score"].sort_values(
    ascending=False
)

print(correlation)