# AI Student Assistant

An AI-powered student support platform that combines machine learning, career guidance, skill-gap analysis, personalized learning recommendations, and student data management.

## Features

* Student performance prediction using TensorFlow
* Skill-gap analysis
* Career recommendations
* Personalized learning roadmap
* Student data storage using MySQL
* Java REST APIs using Spring Boot
* Python ML API using Flask
* Web dashboard using HTML, CSS, and JavaScript
* Java-to-Python AI model integration

## Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Java 21
* Spring Boot
* Spring Data JPA
* REST API

### AI / Machine Learning

* Python
* TensorFlow
* NumPy
* Scikit-learn
* Flask
* Joblib

### Database

* MySQL 8

### Tools

* Git
* GitHub
* VS Code

## System Architecture

```text
                    AI Student Assistant
                           |
                           v
                 HTML / CSS / JavaScript
                           |
                           v
                  Java Spring Boot API
                    /             \
                   /               \
                  v                 v
             MySQL Database     Python Flask API
                                     |
                                     v
                              TensorFlow Model
                                     |
                                     v
                              Predicted Score
```

## Current REST APIs

### Check application

```text
GET /
```

Returns:

```text
AI Student Assistant is running!
```

### Get all students

```text
GET /students
```

### Add a student

```text
POST /students
```

### Predict final score

```text
POST /predict
```

Example prediction input:

```json
{
  "study_hours": 7,
  "attendance": 85,
  "previous_score": 75,
  "assignments_completed": 90,
  "sleep_hours": 7,
  "participation": 80
}
```

Example result:

```json
{
  "predicted_final_score": 77.39
}
```

## Machine Learning Model

The current student performance model uses six input features:

* Study hours
* Attendance
* Previous score
* Assignments completed
* Sleep hours
* Participation

The model is a TensorFlow neural network with scaled input features.

Current evaluation results on the generated dataset:

* MAE: 4.75
* RMSE: 5.87
* R²: 0.6917

> Note: The current dataset is synthetic and was generated for project development and testing. These metrics should not be interpreted as real-world student performance evidence.

## Project Structure

```text
ai-student-assistant/
│
├── career_data/
│   └── career_skills.csv
│
├── data/
│   └── student_performance.csv
│
├── student-assistant/
│   ├── src/
│   │   └── main/
│   │       ├── java/
│   │       └── resources/
│   │           └── static/
│   │               └── dashboard.html
│   ├── pom.xml
│   └── mvnw.cmd
│
├── ml_api.py
├── predict.py
├── train_model.py
├── generate_dataset.py
├── eda.py
├── visualize.py
├── skill_gap.py
├── career_recommendation.py
├── learning_roadmap.py
├── student_performance_model.keras
├── student_performance_scaler.pkl
├── requirements.txt
└── README.md
```

## Running the Project

### 1. Start the Python ML API

```powershell
cd C:\Project\ai-student-assistant
.\.venv\Scripts\activate
python ml_api.py
```

Python ML API:

```text
http://localhost:5000
```

### 2. Start the Spring Boot application

Open another terminal:

```powershell
cd C:\Project\ai-student-assistant\student-assistant
.\mvnw.cmd spring-boot:run
```

Spring Boot:

```text
http://localhost:8080
```

### 3. Open the dashboard

```text
http://localhost:8080/dashboard.html
```

## Database

The project uses a MySQL database named:

```text
ai_student_assistant
```

The main table is:

```text
students
```

Do not commit database passwords or private configuration files to GitHub.

## Future Improvements

* Improve the ML model using real-world datasets
* Add user authentication
* Expand the career and skill database
* Add charts and analytics
* Add prediction history
* Improve the recommendation engine
* Deploy the application online
* Add automated testing and CI/CD

## Author

Developed as an AI/ML engineering portfolio project.

## License

This project is intended for educational and portfolio purposes.
