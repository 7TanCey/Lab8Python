from django.shortcuts import render
from .models import Student, Subject, Exam


def database(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    exams = Exam.objects.all()

    return render(request, 'University_Database/database.html', {'students': students, 'subjects': subjects, 'exams': exams})



