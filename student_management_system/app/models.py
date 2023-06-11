from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    )
    # Add common fields for users in here

    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
        return self.session_start + " To " + self.session_end


class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)

    # these 2 Not required
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class Faculty_Designation(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name) + "_" + str(self.level)


class Faculty(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    faculty_designation = models.ForeignKey(Faculty_Designation, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Staff_Notifications(models.Model):
    staff_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.staff_id.admin.first_name


class Student_Notification(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.student_id.admin.first_name


class Staff_leave(models.Model):
    staff_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name


class Student_leave(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id.admin.first_name + self.staff_id.admin.last_name


class Staff_Feedback(models.Model):
    staff_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name


class Student_Feedback(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name


class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    attendance_data = models.DateField()
    session_year_id = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_id.name + " "


class Attendance_Report(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id.admin.first_name


class StudentResult(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignment_mark = models.IntegerField()
    exam_mark = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id.admin.first_name


class QuestionPaper(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    question_setter_staff_id = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING,
                                                 related_name="question_setter_staff_id")
    reviewer_staff_id = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING, related_name="reviewer_staff_id")
    status = models.IntegerField()
    pdf = models.FileField(upload_to='pdf.files/')
    review_comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_id.name


## Exam Central

class Semester(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=40)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name + "-" + self.abbreviation


# Refer notes for usage. Lines 3-15.
class CourseV2(models.Model):
    name = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.name + "-" + self.duration


# Refer notes for usage. Lines 3-15.
class SessionV2(models.Model):
    courseV2 = models.ForeignKey(CourseV2, on_delete=models.DO_NOTHING, null=True)
    session_start = models.DateTimeField(max_length=100)
    session_end = models.DateTimeField(max_length=100)

    def __str__(self):
        return str(self.courseV2.name) + "_" + str(self.session_start) + "_" + str(self.session_end)


class SubjectV2(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code + "_" + self.name


class Subject_Semester(models.Model):
    subject = models.ForeignKey(SubjectV2, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    session = models.ForeignKey(SessionV2, on_delete=models.DO_NOTHING)
    credits = models.IntegerField(default=0)

    def __str__(self):
        subject_str = str(self.subject) if self.subject.name else "N/A"
        semester_str = str(self.semester) if self.semester.name else "N/A"
        department_str = str(self.department) if self.department.name else "N/A"
        session_str = str(self.session.courseV2) if self.session.courseV2.name else "N/A"
        return subject_str + "_" + semester_str + "_" + department_str + "_" + session_str


class Exam_Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Exam(models.Model):
    subjectSemester = models.ForeignKey(Subject_Semester, on_delete=models.DO_NOTHING, default=None)
    exam_type = models.ForeignKey(Exam_Type, on_delete=models.DO_NOTHING)

    # Roles
    paper_setter_faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING, related_name='paper_setter_faculty', default=0)
    examiner_faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING, related_name='examiner_faculty', default=0)
    moderator_faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING, related_name='moderator_faculty', default=0)
    scrutinizer_faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING, related_name='scrutinizer_faculty', default=0)
    head_examiner_faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING, related_name='head_examiner_faculty', default=0)

    # Exam Papers
    question_paper_from_paper_setter = models.FileField(upload_to='pdf.files/', null=True)
    question_paper_from_moderator = models.FileField(upload_to='pdf.files/', null=True)
    status = models.IntegerField(default=0)
    marks_total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.subjectSemester.subject.name) + "_" + str(self.exam_type.name)


class Student_Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
    marks_obtained = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return str(self.exam) + "_" + "_" + str(self.marks_obtained) + "_" + str(self.status) + "  --->  " + str(self.student)


class Faculty_Subjects(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING)
    subject_semester = models.ForeignKey(Subject_Semester, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.faculty.admin.first_name) + "_" + str(self.subject_semester.subject.name)




