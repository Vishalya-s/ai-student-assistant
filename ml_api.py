from flask import Flask, request, jsonify
import numpy as np
import joblib
from ai_edge_litert.interpreter import Interpreter
import os

app = Flask(__name__)

# Load the TensorFlow Lite model
interpreter = Interpreter(
    model_path="student_performance_model.tflite"
)

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load the scaler
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
    ]], dtype=np.float32)

    student_data_scaled = scaler.transform(student_data)

    interpreter.set_tensor(
        input_details[0]["index"],
        student_data_scaled.astype(np.float32)
    )

    interpreter.invoke()

    prediction = interpreter.get_tensor(
        output_details[0]["index"]
    )

    return jsonify({
        "predicted_final_score": round(float(prediction[0][0]), 2)
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )