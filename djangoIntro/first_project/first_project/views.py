from django.http import HttpResponse

def home(request):
    # print("home page")
    # return HttpResponse("home page")
    return HttpResponse( "<h1>This is Home page</h1>" )  
 