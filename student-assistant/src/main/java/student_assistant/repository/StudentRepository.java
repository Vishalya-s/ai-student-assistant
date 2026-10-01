package student_assistant.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import student_assistant.model.Student;

public interface StudentRepository extends JpaRepository<Student, Integer> {
}