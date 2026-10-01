import pandas as pd
import tensorflow as tf
import joblib

# Load trained model
model = tf.keras.models.load_model("student_performance_model.keras")

# Load scaler
scaler = joblib.load("student_performance_scaler.pkl")

# Get student information
study_hours = float(input("Study hours: "))
attendance = float(input("Attendance (%): "))
previous_score = float(input("Previous score: "))
assignments_completed = float(input("Assignments completed (%): "))
sleep_hours = float(input("Sleep hours: "))
participation = float(input("Participation (%): "))

# Create input data
student_data = pd.DataFrame([[
    study_hours,
    attendance,
    previous_score,
    assignments_completed,
    sleep_hours,
    participation
]], columns=[
    "study_hours",
    "attendance",
    "previous_score",
    "assignments_completed",
    "sleep_hours",
    "participation"
])

# Scale the input
student_data_scaled = scaler.transform(student_data)

# Make prediction
prediction = model.predict(student_data_scaled, verbose=0)

# Display result
print("\n========== PREDICTION ==========")
print(f"Predicted Final Score: {prediction[0][0]:.2f}")