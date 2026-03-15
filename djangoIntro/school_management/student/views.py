from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("student home")

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

    # return HttpResponse("student profile")
    # return render(request, 'student/index.html')
    # return render(request, 'student/index.html', user_data)
    return render(request, 'student/index.html', {"marks" : marks})