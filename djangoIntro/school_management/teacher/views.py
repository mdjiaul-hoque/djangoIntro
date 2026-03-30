from django.shortcuts import render

# Create your views here.

# teacher/profile
def profile(request):
    return render(request, 'teacher/index.html')