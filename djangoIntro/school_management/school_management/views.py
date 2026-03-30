from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# For globalal template render
def home(request):
    # return HttpResponse("<h1>Mother folder's Home</h1>")
    return render(request, 'index.html')