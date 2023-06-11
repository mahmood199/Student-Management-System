from app.models import Course, Session_Year, CustomUser, Student, Subject, QuestionPaper
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app.models import Staff_Notifications, Staff_leave, Staff_Feedback, Attendance, Attendance_Report, \
    StudentResult, Faculty, Exam
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import FileResponse


@login_required(login_url='/')
def HOME(request):
    return render(request, 'staff/home.html')


@login_required(login_url='/')
def NOTIFICATIONS(request):
    staff = Faculty.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_Notifications.objects.filter(staff_id=staff_id)

        context = {
            'notification': notification,
        }
    return render(request, 'staff/notification.html', context)


@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request, status):
    notification = Staff_Notifications.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notifications')


@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Faculty.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_leave.objects.filter(staff_id=staff_id)

        context = {
            'staff_leave_history': staff_leave_history,
        }
    return render(request, 'staff/apply_leave.html', context)


@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff = Faculty.objects.get(admin=request.user.id)

        leave = Staff_leave(
            staff_id=staff,
            data=leave_date,
            message=leave_message,
        )
        leave.save()
        messages.get_messages(request).consume()
        messages.success(request, 'Leave Successfully Sent')
        return redirect('staff_apply_leave')


@login_required(login_url='/')
def STAFF_FEEDBACK(request):
    staff_id = Faculty.objects.get(admin=request.user.id)

    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history': feedback_history,
    }
    return render(request, 'staff/feedback.html', context)


@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')

        staff = Faculty.objects.get(admin=request.user.id)
        feedback = Staff_Feedback(
            staff_id=staff,
            feedback=feedback,
            feedback_reply="",
        )
        feedback.save()
        return redirect('staff_feedback')


@login_required(login_url='/')
def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Faculty.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff=staff_id)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_session_year = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)

            subjects = Subject.objects.filter(id=subject_id)

            for i in subjects:
                student_id = i.coruse_id.id
                students = Student.objects.filter(course=student_id)

    context = {
        'subject': subject,
        'session_year': session_year,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'action': action,
        'students': students,
    }
    return render(request, 'staff/take_attendance.html', context)


@login_required(login_url='/')
def STAFF_SAVE_ATTENDANCE(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')

        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_Year.objects.get(id=session_year_id)

        attendance = Attendance(
            subject_id=get_subject,
            attendance_data=attendance_date,
            session_year_id=get_session_year,
        )

        attendance.save()

        for i in student_id:
            stud_id = i
            int_stud = int(stud_id)

            p_students = Student.objects.get(id=int_stud)
            attendance_report = Attendance_Report(
                student_id=p_students,
                attendance_id=attendance,
            )
            attendance_report.save()

    return redirect('take_attendance')


@login_required(login_url='/')
def STAFF_VIEW_ATTENDANCE(request):
    staff_id = Faculty.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(staff_id=staff_id)
    session_year = Session_Year.objects.all()

    action = request.POST.get('action')

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

    return render(request, 'staff/view_attendance.html', context)


@login_required(login_url='/')
def STAFF_ADD_RESULT(request):
    staff = Faculty.objects.get(admin=request.user.id)

    subjects = Subject.objects.filter(staff_id=staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session_Year.objects.get(id=session_year_id)

            subjects = Subject.objects.filter(id=subject_id)
            for i in subjects:
                student_id = i.course.id
                students = Student.objects.filter(course_id=student_id)

    context = {
        'subjects': subjects,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session': get_session,
        'students': students,
    }

    return render(request, 'staff/add_result.html', context)


@login_required(login_url='/')
def STAFF_SAVE_RESULT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        Exam_mark = request.POST.get('Exam_mark')

        get_student = Student.objects.get(admin=student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exist = StudentResult.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        if check_exist:
            result = StudentResult.objects.get(subject_id=get_subject, student_id=get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = Exam_mark
            result.save()
            messages.get_messages(request).consume()
            messages.success(request, "Successfully Updated Result")
            return redirect('staff_add_result')
        else:
            result = StudentResult(student_id=get_student,
                                   subject_id=get_subject,
                                   exam_marks=Exam_mark,
                                   assignment_mark=assignment_mark)
            result.save()
            messages.get_messages(request).consume()
            messages.success(request, "Successfully Added Result")
            return redirect('staff_add_result')
    return render(request, 'staff/add_result.html')


@login_required(login_url='/')
def STAFF_ADD_QUESTION_PAPER(request):
    subjects = Subject.objects.all()
    staff = Faculty.objects.exclude(admin=request.user.id)
    session_years = Session_Year.objects.all()

    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject = Subject.objects.get(id=subject_id)

        session_year_id = request.POST.get('session_year_id')
        session_year = Session_Year.objects.get(id=session_year_id)

        question_setter_staff = Faculty.objects.get(admin=request.user.id)

        reviewer_staff_id = request.POST.get('reviewer_staff_id')
        print(reviewer_staff_id)

        reviewer_staff = Faculty.objects.get(id=reviewer_staff_id)
        print(reviewer_staff.admin.first_name)
        print(reviewer_staff.admin.last_name)

        question_paper_pdf = request.FILES.get('question_paper')

        question_paper = QuestionPaper(
            subject_id=subject,
            session_year_id=session_year,
            question_setter_staff_id=question_setter_staff,
            reviewer_staff_id=reviewer_staff,
            status=0,
            pdf=question_paper_pdf,
            review_comments=""
        )
        question_paper.save()
        messages.get_messages(request).consume()
        messages.success(request, "Question Paper added successfully")
        return redirect('staff_view_all_question_papers')

    context = {
        'subject': subjects,
        'staff': staff,
        'session_year': session_years,
    }

    return render(request, 'staff/add_question_paper.html', context)


@login_required(login_url='/')
def VIEW_ALL_QUESTION_PAPERS(request):
    logged_in_user = Faculty.objects.get(admin=request.user.id)

    if logged_in_user is not None:
        print("Debugging starts here")
        print(str(logged_in_user))
        print(str(logged_in_user.admin.first_name))
        print(str(logged_in_user.admin.last_name))
        filtered_papers = QuestionPaper.objects.filter(
            Q(question_setter_staff_id=logged_in_user) | Q(reviewer_staff_id=logged_in_user)
        )
    else:
        filtered_papers = QuestionPaper.objects.all()

    context = {
        'logged_in_user': logged_in_user,
        'question_papers': filtered_papers,
    }

    return render(request, 'staff/view_all_question_papers.html', context)


@login_required(login_url='/')
def EDIT_QUESTION_PAPER(request, id):
    question_paper = QuestionPaper.objects.get(id=id)
    context = {
        'question_paper': question_paper,
    }
    return render(request, 'staff/edit_question_paper.html', context)


@login_required(login_url='/')
def REVIEW_QUESTION_PAPER(request, id):
    question_paper = QuestionPaper.objects.get(id=id)
    context = {
        'question_paper': question_paper,
    }
    return render(request, 'staff/review_question_paper.html', context)


@login_required(login_url='/')
def APPROVE_QUESTION_PAPER(request, id):
    if request.method == "POST":
        id = request.POST.get('id')
        question_paper = QuestionPaper.objects.get(id=id)

        question_paper.status = 2
        question_paper.save()

        messages.success(request, 'Question Paper approved!')
        return redirect('staff_view_all_question_papers')

    return render(request, 'staff/review_question_paper.html')


@login_required(login_url='/')
def ADD_COMMENTS_ON_QUESTION_PAPER(request):
    if request.method == "POST":
        review_comments = request.POST.get('review_comments')
        id = request.POST.get('id')

        print("Question paper ---> " + str(id))
        print("Question review comments ---> " + str(review_comments))

        question_paper = QuestionPaper.objects.get(id=id)

        question_paper.review_comments = review_comments
        question_paper.status = 1
        question_paper.save()

        messages.success(request, 'Review added for question paper!')
        return redirect('staff_view_all_question_papers')

    return render(request, 'staff/review_question_paper.html')


@login_required(login_url='/')
def VIEW_ALL_QUESTION_PAPER(request, id):
    question_paper = QuestionPaper.objects.get(id=id)
    context = {
        'question_paper': question_paper,
    }
    return render(request, 'staff/view_question_paper.html', context)


# this staff will set ques paper
@login_required(login_url='/')
def STAFF_SETTER(request):
    return render(request, 'staff/staff_setter.html')


@login_required(login_url='/')
def STAFF_MODERATOR(request):
    return render(request, 'staff/staff_moderator.html')


@login_required(login_url='/')
def STAFF_EXAMINER(requesrt):
    return render(requesrt, 'staff/staff_examiner.html')


@login_required(login_url='/')
def STAFF_SCRUTINIZER(requesrt):
    return render(requesrt, 'staff/staff_scrutinizer.html')


@login_required(login_url='/')
def STAFF_HEAD_EXAMINER(requesrt):
    return render(requesrt, 'staff/staff_head_examiner.html')


@login_required(login_url='/')
def VIEW_MY_EXAM_ROLES(request):
    logged_in_user = Faculty.objects.get(admin=request.user.id)

    exams = Exam.objects.filter(
        Q(paper_setter_faculty=logged_in_user) |
        Q(examiner_faculty=logged_in_user) |
        Q(moderator_faculty=logged_in_user) |
        Q(scrutinizer_faculty=logged_in_user) |
        Q(head_examiner_faculty=logged_in_user)
    )

    context = {
        'exams': exams,
        'logged_in_user': logged_in_user
    }

    return render(request, 'staff/view_my_exam_roles.html', context)


@login_required(login_url='/')
def UPDATE_QUESTION_PAPER(request):
    if request.method == "POST":
        id = request.POST.get('id')
        question_paper_pdf_file = request.POST.get('question_paper')

        question_paper = QuestionPaper.objects.get(id=id)
        question_paper.pdf = question_paper_pdf_file

        question_paper.save()
        messages.get_messages(request).consume()
        messages.success(request, 'Question paper updated successfully')
        return redirect('view_all_question_papers')

    return render(request, 'staff/edit_question_paper.html')


@login_required(login_url='/')
def SETTER_ADD_QUESTION_PAPER(request, id):
    if request.method == "POST":
        exam_id = request.POST.get('id')
        exam = Exam.objects.get(id=exam_id)
        question_paper_pdf = request.FILES.get('question_paper_pdf')

        exam.question_paper_from_paper_setter.save(question_paper_pdf.name, question_paper_pdf)

        exam.status = 1
        exam.save()
        messages.success(request, 'Added question paper for setter')
        return redirect('setter_add_question_paper', id=exam_id)

    exam = Exam.objects.get(id=id)
    context = {
        'exam': exam
    }
    return render(request, 'staff/setter_question_paper_for_exam.html', context)


@login_required(login_url='/')
def MODERATOR_ADD_QUESTION_PAPER(request, id):
    if request.method == "POST":
        exam_id = request.POST.get('id')
        exam = Exam.objects.get(id=exam_id)
        question_paper_pdf = request.FILES.get('question_paper_pdf')

        exam.question_paper_from_moderator.save(question_paper_pdf.name, question_paper_pdf)

        exam.status = 2
        exam.save()
        messages.success(request, 'Added for question paper  for moderator')
        return redirect('moderator_add_question_paper', id=exam_id)

    exam = Exam.objects.get(id=id)
    context = {
        'exam': exam
    }
    return render(request, 'staff/moderator_question_paper_for_exam.html', context)


@login_required(login_url='/')
def DOWNLOAD_QUESTION_PAPER_PDF(request, id):
    try:
        question_paper = QuestionPaper.objects.get(id=id)
        file_path = question_paper.pdf.path
        subject_name = question_paper.subject_id.name
        session_year_name = question_paper.session_year_id.session_start + "_to_" + question_paper.session_year_id.session_end
        file_name = subject_name + "_" + session_year_name + "_" + str(id) + ".pdf"

        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{file_name}"'
            return response
    except QuestionPaper.DoesNotExist:
        return HttpResponseNotFound("Question paper not found")


@login_required(login_url='/')
def VIEW_QUESTION_PAPER(request, id):
    try:
        exam = Exam.objects.get(id=id)
        print(str(exam.question_paper_from_moderator))
        file_path = exam.question_paper_from_moderator.path
        subject_name = exam.subjectSemester.subject.name
        session_year_name = str(exam.subjectSemester.session.session_start) + "_to_" + str(exam.subjectSemester.session.session_end)
        file_name = subject_name + "_" + session_year_name + "_" + str(id) + ".pdf"

        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{file_name}"'
            return response
    except Exam.DoesNotExist:
        return HttpResponseNotFound("Question paper not found")
