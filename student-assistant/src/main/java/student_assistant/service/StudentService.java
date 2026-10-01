package student_assistant.service;

import org.springframework.stereotype.Service;
import student_assistant.model.Student;
import student_assistant.repository.StudentRepository;

import java.util.List;

@Service
public class StudentService {

    private final StudentRepository studentRepository;

    public StudentService(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    public List<Student> getAllStudents() {
        return studentRepository.findAll();
    }
    public Student saveStudent(Student student) {
    return studentRepository.save(student);
    }
}