from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, College
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

# Hardcoded credentials for the login page
USERNAME = "Mr.Ra"
PASSWORD = "Password"

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == USERNAME and password == PASSWORD:
            return redirect('select_college')
        else:
            return render(request, 'students/login.html', {
                'error': 'Invalid username or password. Please try again.'
            })

    return render(request, 'students/login.html')

def select_college(request):
    colleges = College.objects.all()
    students_data = {
        college.id: [
            {'id': student.id, 'name': student.name}
            for student in college.students.all()
        ]
        for college in colleges
    }

    if request.method == 'POST':
        college_id = request.POST.get('college')
        student_id = request.POST.get('student')

        if not college_id or not student_id:
            return render(request, 'students/select_college.html', {
                'error': 'Please select both a college and a candidate.',
                'colleges': colleges,
                'students_json': students_data,
            })

        return redirect('resume_page', student_id=student_id)

    return render(request, 'students/select_college.html', {
        'colleges': colleges,
        'students_json': students_data,
    })

def resume_page(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        feedback = request.POST.get('feedback', '').strip()
        resume_content = request.POST.get('resume_content', '').strip()

        if feedback or resume_content:
            email_message = f"""
            Feedback for {student.name}:

            {feedback}

            Resume Content Submitted:

            {resume_content}
            """

            email = EmailMessage(
                subject=f"Feedback and Resume for {student.name}",
                body=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['shekharpatil9120@gmail.com'],  # Replace with desired recipient
            )
            email.send(fail_silently=False)

            return render(request, 'students/resume.html', {
                'student': student,
                'message': 'Feedback and resume submitted successfully and emailed.',
            })

        return render(request, 'students/resume.html', {
            'student': student,
            'error': 'Feedback or resume content cannot be empty.',
        })

    return render(request, 'students/resume.html', {'student': student})
