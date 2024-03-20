from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/',views.student, name='alumn'),  
    path('teacher/', views.teacher, name='prof'),
    path('teacher/teachers/<str:pk>', views.teachers, name ='teacher'),
    path('student/students/<str:pk>', views.students, name ='student'),
    path('student_form/', views.student_form, name='student_form'),
    path('teacher_form/', views.teacher_form, name='teacher_form')
]
