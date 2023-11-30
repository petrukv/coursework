from django.shortcuts import render
from .models import Student


# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request, 'applicants/index.html', {'students' : students})

def input(request):
    students = Student.objects.all()

    students_data = list(students.values())
    for student in students_data:
        math_rating = float(student['math_rating'])
        ukr_rating = float(student['ukr_rating'])
        hist_rating = float(student['hist_rating'])
        
        student['average_rating'] = math_rating * 0.5 + ukr_rating * 0.3 + hist_rating * 0.2

    if 'numberOfStudents' in request.GET:
        number_of_students = int(request.GET['numberOfStudents'])
        students_data = sorted(students_data, key=lambda s: s['average_rating'], reverse=True)[:number_of_students]

    return render(request, 'applicants/input.html', {'students': students_data})


def interview(request):
    students = Student.objects.all()

    students_data = list(students.values())
    for student in students_data:
        math_rating = float(student['math_rating'])
        ukr_rating = float(student['ukr_rating'])
        hist_rating = float(student['hist_rating'])
        
        student['average_rating'] = round(math_rating * 0.5 + ukr_rating * 0.3 + hist_rating * 0.2, 2)

    if 'numberOfStudents' in request.GET:
        number_of_students = int(request.GET['numberOfStudents'])
        students_data = sorted(students_data, key=lambda s: s['average_rating'], reverse=True)[:number_of_students]

    if 'passingGrade' in request.GET:
        passing_grade = float(request.GET['passingGrade'])
        students_data = [student for student in students_data if student['average_rating'] >= passing_grade and not student['selfpaying']]

    return render(request, 'applicants/interview.html', {'students': students_data})


def bio(request, pk):
    student = Student.objects.get(id = pk)
    context = {
            'student': student,
        }
    return render(request, 'applicants/student.html', context)
