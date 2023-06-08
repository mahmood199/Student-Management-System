from app.models import Course, Session_Year, CustomUser, Student, Staff, Subject, Staff_Notifications, Staff_leave, \
    Staff_Feedback, Student_Notification, Student_Feedback, Student_leave, Attendance, Attendance_Report, CourseV2, \
    QuestionPaper, \
    Semester, Department, Exam_Type, SessionV2, SubjectV2, Faculty_Designation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    print("student_count = " + str(student_count))
    staff_count = Staff.objects.all().count()
    print("staff_count = " + str(staff_count))
    course_count = CourseV2.objects.all().count()
    print("course_count = " + str(course_count))
    subject_count = SubjectV2.objects.all().count()
    print("subject_count = " + str(subject_count))

    student_gender_male = Student.objects.filter(gender='Male').count()
    print("student_gender_male = " + str(student_gender_male))
    student_gender_female = Student.objects.filter(gender='Female').count()
    print("student_gender_female = " + str(student_gender_female))

    context = {
        'student_count': student_count,
        'staff_count': staff_count,
        'course_count': course_count,
        'subject_count': subject_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
    }

    return render(request, 'hod/home.html', context)


@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                course_id=course,
                gender=gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('add_student')

    context = {
        'course': course,
        'session_year': session_year,
    }

    return render(request, 'hod/add_student.html', context)


@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student': student,
    }
    return render(request, 'hod/view_student.html', context)


@login_required(login_url='/')
def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'student': student,
        'course': course,
        'session_year': session_year,
    }
    return render(request, 'hod/edit_student.html', context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id=student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id=course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id=session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request, 'Record Are Successfully Updated !')
        return redirect('view_student')

    return render(request, 'hod/edit_student.html')


@login_required(login_url='/')
def DELETE_STUDENT(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, 'Record Are Successfully Deleted !')
    return redirect('view_student')


@login_required(login_url='/')
def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
            name=course_name,
        )
        course.save()
        messages.success(request, 'Course Are Successfully Created ')

        return redirect('view_course')

    return render(request, 'hod/add_course.html')


@login_required(login_url='/')
def VIEW_COURSE(request):
    course = CourseV2.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'hod/view_course.html', context)


@login_required(login_url='/')
def EDIT_COURSE(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request, 'hod/edit_course.html', context)


@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request, 'Course Are Successfully Updated ')
        return redirect('view_course')

    return render(request, 'hod/edit_course.html')


@login_required(login_url='/')
def DELETE_COURSE(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course are Successfully Deleted')

    return redirect('view_course')


@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        print(profile_pic, first_name, last_name, email, username, password, address, gender)

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already taken !')
            return redirect('add_staff')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username already taken !')
            return redirect('add_staff')

        else:
            user = CustomUser(first_name=first_name, last_name=last_name, email=email, profile_pic=profile_pic,
                              username=username, user_type=2)
            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                address=address,
                gender=gender
            )
            staff.save()
            messages.success(request, "Staff is successfully added !")
            return redirect("view_staff")

    return render(request, "hod/add_staff.html")


@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff,
    }
    return render(request, "hod/view_staff.html", context)


@login_required(login_url='/')
def EDIT_STAFF(request, id):
    staff = Staff.objects.get(id=id)

    context = {
        'staff': staff
    }

    return render(request, "hod/edit_staff.html", context)


@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        staff_id = request.POST.get('staff_id')

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()

        messages.success(request, "Staff is updated successfully")
        return redirect('view_staff')

    return render(request, "hod/edit_staff.html")


@login_required(login_url='/')
def DELETE_STAFF(request, admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()

    messages.success(request, "Records deleted successfully!")

    return redirect('view_staff')


@login_required(login_url='/')
def ADD_SUBJECT(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name=subject_name,
            course=course,
            staff=staff,
        )
        subject.save()
        messages.success(request, "Subject added successfully")
        return redirect('view_subject')

    context = {
        'course': course,
        'staff': staff
    }

    return render(request, 'hod/add_subject.html', context)


@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    context = {
        'subject': subject
    }

    return render(request, 'hod/view_subject.html', context)


@login_required(login_url='/')
def EDIT_SUBJECT(request, id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()

    context = {
        'subject': subject,
        'course': course,
        'staff': staff,
    }

    return render(request, 'edit_subject.html', context)


@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            id=subject_id,
            name=subject_name,
            course=course,
            staff=staff
        )

        subject.save()
        messages.success(request, 'Subject updated successfully')
        return redirect('view_subject')

    return None


@login_required(login_url='/')
def DELETE_SUBJECT(request, id):
    subject = Subject.objects.filter(id=id)
    subject.delete()

    messages.success(request, 'Subject deleted successfully')

    return redirect('view_subject')


@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            session_start=session_year_start,
            session_end=session_year_end
        )
        session.save()
        messages.success(request, 'Session added successfully')
        return redirect('view_session')

    return render(request, 'hod/add_session.html')


@login_required(login_url='/')
def VIEW_SESSION(request):
    session = Session_Year.objects.all()
    context = {
        'session': session
    }

    return render(request, 'hod/view_session.html', context)


@login_required(login_url='/')
def EDIT_SESSION(request, id):
    session = Session_Year.objects.filter(id=id)

    context = {
        'session': session
    }

    return render(request, 'hod/edit_session.html', context)


@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            id=session_id,
            session_start=session_year_start,
            session_end=session_year_end
        )

        session.save()
        messages.success(request, "Session updated successfully")
        return redirect('view_session')

    return None


@login_required(login_url='/')
def DELETE_SESSION(request, id):
    session = Session_Year.objects.filter(id=id)
    session.delete()

    messages.success(request, "Session deleted successfully")

    return redirect('view_session')


@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notifications.objects.all().order_by('-id')[0:5]

    context = {
        'staff': staff,
        'see_notification': see_notification,
    }
    return render(request, 'hod/staff_notification.html', context)


@login_required(login_url='/')
def SAVE_STAFF_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=staff_id)
        notification = Staff_Notifications(
            staff_id=staff,
            message=message,
        )
        notification.save()
        messages.success(request, 'Notification Are Successfully Sent')
        return redirect('staff_send_notification')


@login_required(login_url='/')
def Staff_Leave_view(request):
    staff_leave = Staff_leave.objects.all()

    context = {
        'staff_leave': staff_leave,
    }
    return render(request, 'hod/staff_leave.html', context)


@login_required(login_url='/')
def STAFF_APPROVE_LEAVE(request, id):
    leave = Staff_leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')


@login_required(login_url='/')
def STAFF_DISAPPROVE_LEAVE(request, id):
    leave = Staff_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')


@login_required(login_url='/')
def STUDENT_LEAVE_VIEW(request):
    student_leave = Student_leave.objects.all()
    context = {
        'student_leave': student_leave,
    }
    return render(request, 'hod/student_leave.html', context)


@login_required(login_url='/')
def STUDENT_APPROVE_LEAVE(request, id):
    leave = Student_leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')


@login_required(login_url='/')
def STUDENT_DISAPPROVE_LEAVE(request, id):
    leave = Student_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')


@login_required(login_url='/')
def STAFF_FEEDBACK(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all().order_by('-id')[0:5]
    context = {
        'feedback': feedback,
        'feedback_history': feedback_history,
    }
    return render(request, 'hod/staff_feedback.html', context)


@login_required(login_url='/')
def STUDENT_FEEDBACK(request):
    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all().order_by('-id')[0:5]
    context = {
        'feedback': feedback,
        'feedback_history': feedback_history,
    }
    return render(request, 'hod/student_feedback.html', context)


@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply

        feedback.status = 1

        feedback.save()
        return redirect('staff_feedback_reply')


@login_required(login_url='/')
def REPLY_STUDENT_FEEDBACK(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Student_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply

        feedback.status = 1

        feedback.save()
        return redirect('get_student_feedback')


@login_required(login_url='/')
def STUDENT_SEND_NOTIFICATION(request):
    student = Student.objects.all()
    notification = Student_Notification.objects.all()
    context = {
        'student': student,
        'notification': notification,
    }
    return render(request, 'hod/student_notification.html', context)


@login_required(login_url='/')
def SAVE_STUDENT_NOTIFICATION(request):
    if request.method == "POST":
        message = request.POST.get('message')
        student_id = request.POST.get('student_id')

        student = Student.objects.get(admin=student_id)

        stud_notification = Student_Notification(
            student_id=student,
            message=message,
        )
        stud_notification.save()
        messages.success(request, 'Student Notification Are Successfully Sent')
        return redirect('student_send_notification')


@login_required(login_url='/')
def VIEW_ATTENDANCE(request):
    print(request)
    print(request.user)
    print(request.user.id)
    staff_id = Staff.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(staff_id=staff_id)
    session_year = Session_Year.objects.all()

    action = request.Get.get('action')

    get_subject = None
    attendance_date = None
    get_session_year = None
    attendance_report = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)
            attendance = Attendance.objects.filter(subject_id=get_subject, attendance_data=attendance_date)

            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id=attendance_id)

    context = {
        'subject': subject,
        'session_year': session_year,
        'action': action,
        'attendance_date': attendance_date,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'attendance_report': attendance_report,
    }
    return render(request, 'hod/view_attendance.html', context)


@login_required(login_url='/')
def PROFILE(request):
    return render(request, 'hod/profile.html')


@login_required(login_url='/')
def VIEW_ALL_EXAM_ROLES(request):
    return render(request, 'hod/view_all_exam_roles.html')


@login_required(login_url='/')
def ASSIGN_EXAM_ROLE(request):
    return render(request, 'hod/assign_exam_roles.html')


@login_required(login_url='/')
def ADD_SEMESTER(request):
    if request.method == "POST":
        name = request.POST.get('semester')
        semester = Semester(
            name=name,
        )
        semester.save()
        messages.success(request, 'Semester Entry Successful ')
        return redirect('view_semester')
    return render(request, 'hod/add_semester.html')


@login_required(login_url='/')
def VIEW_SEMESTER(request):
    semester = Semester.objects.all()
    context = {
        'semester': semester,
    }
    return render(request, 'hod/view_semester.html', context)


@login_required(login_url='/')
def ADD_DEPARTMENT(request):
    if request.method == "POST":
        name = request.POST.get('department_name')
        abbreviation = request.POST.get('department_abbreviation')
        department = Department(
            name=name,
            abbreviation=abbreviation,
        )
        department.save()
        messages.success(request, 'Department Entry Successful ')
        return redirect('view_department')
    return render(request, 'hod/add_department.html')


@login_required(login_url='/')
def VIEW_DEPARTMENT(request):
    department = Department.objects.all()
    context = {
        'department': department,
    }
    return render(request, 'hod/view_department.html', context)


@login_required(login_url='/')
def ADD_EXAM_TYPE(request):
    if request.method == "POST":
        name = request.POST.get('exam_type')
        exam_type = Exam_Type(
            name=name,
        )
        exam_type.save()
        messages.success(request, 'Exam Type Entry Successful ')
    return render(request, 'hod/add_exam_type.html')


@login_required(login_url='/')
def ADD_SESSION_V2(request):
    if request.method == "POST":
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        course_v2 = request.POST.get('courseV2')
        session_v2 = SessionV2(
            session_start=session_start,
            session_end=session_end,
            course_v2=course_v2,
        )
        session_v2.save()
        messages.success(request, 'Session Entry Successful ')
    courses = CourseV2.objects.all()
    context = {
        'course': courses
    }
    return render(request, 'hod/add_session_v2.html', context)


@login_required(login_url='/')
def VIEW_SESSION_V2(request):
    sessions = SessionV2.objects.all()
    context = {
        'sessions': sessions,
    }
    return render(request, 'hod/view_session_v2.html', context)


@login_required(login_url='/')
def ADD_COURSE_V2(request):
    if request.method == "POST":
        name = request.POST.get('course_name_v2')
        duration = request.POST.get('duration')
        course = CourseV2(
            name=name,
            duration=duration,
        )
        course.save()
        messages.success(request, 'Course Entry Successful ')
        redirect('add_course_v2')
    return render(request, 'hod/add_course_v2.html')


@login_required(login_url='/')
def ADD_SUBJECT_V2(request):
    if request.method == "POST":
        code = request.POST.get('code')
        name = request.POST.get('name')
        subject_v2 = SubjectV2(
            code=code,
            name=name,
        )
        subject_v2.save()
        messages.success(request, 'Subject Entry Successful ')
    return render(request, 'hod/add_subject_v2.html')


@login_required(login_url='/')
def VIEW_SUBJECT_V2(request):
    subjects = SubjectV2.objects.all()
    context = {
        'subjects': subjects,
    }
    return render(request, 'hod/view_subject_v2.html', context)


@login_required(login_url='/')
def ADD_FACULTY(request):
    if request.method == "POST":
        name = request.POST.get('faculty_designation_name')
        level = request.POST.get('faculty_designation_level')
        print("Name:" + str(name))
        print("Level:" + str(level))
        faculty = Faculty_Designation(
            name=name,
            level=level,
        )
        faculty.save()
        messages.success(request, 'Faculty Entry Successful ')
        return redirect('view_faculty')
    return render(request, 'hod/add_faculty.html')


@login_required(login_url='/')
def VIEW_FACULTY(request):
    faculty_designations = Faculty_Designation.objects.all()
    context = {
        'faculty_designations': faculty_designations
    }
    return render(request, 'hod/view_faculty.html', context)
