package student_assistant.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import student_assistant.ml.MlPredictionService;
import student_assistant.model.Student;
import student_assistant.service.StudentService;

import java.util.List;
import java.util.Map;

@RestController
public class StudentController {

    private final StudentService studentService;
    private final MlPredictionService mlPredictionService;

    public StudentController(
            StudentService studentService,
            MlPredictionService mlPredictionService) {
        this.studentService = studentService;
        this.mlPredictionService = mlPredictionService;
    }

    @GetMapping("/")
    public String home() {
        return "AI Student Assistant is running!";
    }

    @GetMapping("/students")
    public List<Student> getAllStudents() {
        return studentService.getAllStudents();
    }

    @PostMapping("/students")
    public Student addStudent(@RequestBody Student student) {
        return studentService.saveStudent(student);
    }

    @PostMapping("/predict")
    public Map<String, Object> predictScore(
            @RequestBody Map<String, Object> studentData) {
        return mlPredictionService.predictScore(studentData);
    }
}