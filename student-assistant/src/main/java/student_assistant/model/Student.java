package student_assistant.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "students")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer studentId;

    private String name;
    private String email;
    private Float studyHours;
    private Float attendance;
    private Float previousScore;
    private Float assignmentsCompleted;
    private Float sleepHours;
    private Float participation;

    public Student() {
    }

    public Integer getStudentId() {
        return studentId;
    }

    public void setStudentId(Integer studentId) {
        this.studentId = studentId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Float getStudyHours() {
        return studyHours;
    }

    public void setStudyHours(Float studyHours) {
        this.studyHours = studyHours;
    }

    public Float getAttendance() {
        return attendance;
    }

    public void setAttendance(Float attendance) {
        this.attendance = attendance;
    }

    public Float getPreviousScore() {
        return previousScore;
    }

    public void setPreviousScore(Float previousScore) {
        this.previousScore = previousScore;
    }

    public Float getAssignmentsCompleted() {
        return assignmentsCompleted;
    }

    public void setAssignmentsCompleted(Float assignmentsCompleted) {
        this.assignmentsCompleted = assignmentsCompleted;
    }

    public Float getSleepHours() {
        return sleepHours;
    }

    public void setSleepHours(Float sleepHours) {
        this.sleepHours = sleepHours;
    }

    public Float getParticipation() {
        return participation;
    }

    public void setParticipation(Float participation) {
        this.participation = participation;
    }
}