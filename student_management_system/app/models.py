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


# Not a good practice

class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)

    # these 2 Not required.Add designation, joining date etc etc
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username


class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Staff_Notifications(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
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
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
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
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
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
    question_setter_staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING,
                                                 related_name="question_setter_staff_id")
    reviewer_staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name="reviewer_staff_id")
    status = models.IntegerField()
    pdf = models.FileField(upload_to='pdf.files/')
    review_comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_id.name


## Exam Central

class Semester(models.Model):
    name = models.CharField(max_length=10)

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
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session_start = models.DateTimeField(max_length=100)
    session_end = models.DateTimeField(max_length=100)

    def __str__(self):
        return self.course + "_" + self.session_start + "_" + self.session_end


class SubjectV2(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code + "_" + self.name


class Subject_Semester(models.Model):
    subject = models.ForeignKey(SubjectV2, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    session = models.ForeignKey(SessionV2, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject + "_" + self.semester + "_" + self.department + "_" + self.session


class Exam_Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Faculty_Designation(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return str(self.name) + "_" + str(self.level)


class Faculty(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    faculty_designation = models.ForeignKey(Faculty_Designation, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.admin) + "_" + str(self.address) + "_" + str(self.gender) + "_" + str(self.faculty_designation)


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_type = models.ForeignKey(Exam_Type, on_delete=models.CASCADE)
    marks_total = models.IntegerField()

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseV2, on_delete=models.CASCADE)

    session = models.ForeignKey(SessionV2, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    # Roles
    paper_setter_faculty = models.ManyToManyField(Faculty, related_name='paper_setter_faculty')
    examiner_faculty = models.ManyToManyField(Faculty, 'examiner_faculty')
    moderator_faculty = models.ManyToManyField(Faculty, 'moderator_faculty')
    scrutinizer_faculty = models.ManyToManyField(Faculty, 'scrutinizer_faculty')
    head_examiner_faculty = models.ManyToManyField(Faculty, 'head_examiner_faculty')

    # Exam Papers
    question_paper_from_paper_setter = models.FileField(upload_to='pdf.files/', null=True)
    question_paper_from_moderator = models.FileField(upload_to='pdf.files/', null=True)
    status = models.IntegerField()

    def __str__(self):
        return (
                str(self.subject) + "_" + str(self.department) + "_" + str(self.course) + "_" +
                str(self.session) + "_" + str(self.semester)
        )


class Student_Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_type = models.ForeignKey(Exam_Type, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return str(self.exam) + "_" + str(self.student) + "_" + str(self.subject) + "_" + \
               str(self.exam_type) + "_" + str(self.marks_obtained) + "_" + str(self.status)




class Faculty_Subjects(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject_semester = models.ForeignKey(Subject_Semester, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.faculty) + "_" + str(self.subject_semester)




