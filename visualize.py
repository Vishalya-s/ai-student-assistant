import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/student_performance.csv")

# Study hours vs final score
plt.figure(figsize=(8, 5))
plt.scatter(df["study_hours"], df["final_score"], alpha=0.5)
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")
plt.grid(True)
plt.show()

# Previous score vs final score
plt.figure(figsize=(8, 5))
plt.scatter(df["previous_score"], df["final_score"], alpha=0.5)
plt.xlabel("Previous Score")
plt.ylabel("Final Score")
plt.title("Previous Score vs Final Score")
plt.grid(True)
plt.show()

# Attendance vs final score
plt.figure(figsize=(8, 5))
plt.scatter(df["attendance"], df["final_score"], alpha=0.5)
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")
plt.grid(True)
plt.show()

# Correlation matrix
plt.figure(figsize=(9, 7))
correlation = df.corr(numeric_only=True)

plt.imshow(correlation, cmap="coolwarm", aspect="auto")
plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Feature Correlation Matrix")
plt.tight_layout()
plt.show()