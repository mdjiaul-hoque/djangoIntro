from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

# student/home
def home(request):
    return HttpResponse("<h1>Student's Home</h1>")


#student info delete
def delete_student(request, id):
        student = models.Student.object.get(id = id)
        student.delete()
        return HttpResponse("Student delete successfully")

# student/profile
def profile(request):

    user_data = {
        "name" : "Abdur Rahim",
        "age"  : 20
    }

    
    marks = [
        {
            "id" : 1,
            "subject" : "english",
            "mark" : 90
        },
        {
            "id" : 2,
            "subject" : "banglish",
            "mark" : 80
        },
        {
            "id" : 3,
            "subject" : "math",
            "mark" : 70
        },
        {
            "id" : 4,
            "subject" : "scince",
            "mark" : 60
        }
            ]
    
    student_data=models.Student.objects.all()
    # print(student_data)

    # return HttpResponse("student profile")

    # template render
    # return render(request, 'student/index.html')
    # return render(request, 'student/index.html', user_data)

    # template render with json data
    return render(request, 'student/index.html', {"marks" : marks, 'student_data': student_data})







