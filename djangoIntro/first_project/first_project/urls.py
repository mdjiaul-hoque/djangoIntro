from django.contrib import admin
from django.urls import path
# from views import home
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', home),
    path('home/', views.home),
]
