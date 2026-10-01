import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------

df = pd.read_csv("data/student_performance.csv")

print("Dataset loaded successfully!")
print("Shape:", df.shape)

# --------------------------------------------------
# 2. Separate features and target
# --------------------------------------------------

X = df[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "assignments_completed",
        "sleep_hours",
        "participation",
    ]
]

y = df["final_score"]

# --------------------------------------------------
# 3. Train / test split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# --------------------------------------------------
# 4. Feature scaling
# --------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --------------------------------------------------
# 5. Build TensorFlow neural network
# --------------------------------------------------

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(6,)),

    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(16, activation="relu"),

    tf.keras.layers.Dense(1)
])

# --------------------------------------------------
# 6. Compile model
# --------------------------------------------------

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

print("\nModel created successfully!")

# --------------------------------------------------
# 7. Train model
# --------------------------------------------------
early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True
)

history = model.fit(
    X_train_scaled,
    y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=32,
    callbacks=[early_stopping],
    verbose=1
)

# --------------------------------------------------
# 8. Make predictions
# --------------------------------------------------

predictions = model.predict(X_test_scaled).flatten()

# --------------------------------------------------
# 9. Evaluate model
# --------------------------------------------------

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("\n========== MODEL PERFORMANCE ==========")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# --------------------------------------------------
# 10. Show sample predictions
# --------------------------------------------------

print("\n========== SAMPLE PREDICTIONS ==========")

for actual, predicted in zip(
    y_test.iloc[:10],
    predictions[:10]
):
    print(
        f"Actual: {actual:.2f} | "
        f"Predicted: {predicted:.2f}"
    )

# --------------------------------------------------
# 11. Save model
# --------------------------------------------------

model.save("student_performance_model.keras")
joblib.dump(scaler, "student_performance_scaler.pkl")

print("\nModel saved successfully!")
print("Scaler saved successfully!")