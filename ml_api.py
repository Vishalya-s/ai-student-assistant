from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import joblib

app = Flask(__name__)

# Load the trained TensorFlow model
model = tf.keras.models.load_model("student_performance_model.keras")

# Load the scaler used during training
scaler = joblib.load("student_performance_scaler.pkl")


@app.route("/")
def home():
    return "AI Student Assistant ML API is running!"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    student_data = np.array([[
        data["study_hours"],
        data["attendance"],
        data["previous_score"],
        data["assignments_completed"],
        data["sleep_hours"],
        data["participation"]
    ]])

    student_data_scaled = scaler.transform(student_data)

    prediction = model.predict(student_data_scaled, verbose=0)

    return jsonify({
        "predicted_final_score": round(float(prediction[0][0]), 2)
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)