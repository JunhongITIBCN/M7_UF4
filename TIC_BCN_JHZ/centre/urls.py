from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/',views.student, name='alumn'),  
    path('teacher/<int:pk>', views.teacher, name='prof'),
]