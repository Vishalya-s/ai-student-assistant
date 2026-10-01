import pandas as pd
import numpy as np

np.random.seed(42)

number_of_students = 1000

data = {
    "study_hours": np.round(np.random.uniform(1, 10, number_of_students), 1),
    "attendance": np.round(np.random.uniform(50, 100, number_of_students), 1),
    "previous_score": np.round(np.random.uniform(40, 95, number_of_students), 1),
    "assignments_completed": np.round(
        np.random.uniform(40, 100, number_of_students), 1
    ),
    "sleep_hours": np.round(np.random.uniform(4, 9, number_of_students), 1),
    "participation": np.round(np.random.uniform(30, 100, number_of_students), 1),
}

df = pd.DataFrame(data)

# Generate a realistic final score
df["final_score"] = (
    0.25 * df["study_hours"] * 10
    + 0.20 * df["attendance"]
    + 0.25 * df["previous_score"]
    + 0.15 * df["assignments_completed"]
    + 0.05 * df["sleep_hours"] * 10
    + 0.10 * df["participation"]
)

# Add a small amount of randomness
noise = np.random.normal(0, 5, number_of_students)
df["final_score"] += noise

# Keep scores between 0 and 100
df["final_score"] = df["final_score"].clip(0, 100)

# Round values
df = df.round(2)

# Save dataset
file_path = "data/student_performance.csv"
df.to_csv(file_path, index=False)

print("Dataset created successfully!")
print(f"Number of students: {len(df)}")
print(f"Saved to: {file_path}")
print("\nFirst 5 rows:")
print(df.head())