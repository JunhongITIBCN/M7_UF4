from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/',views.student, name='alumn'),  
    path('teacher/', views.teacher, name='prof'),
    path('update-student/<str:pk>/', views.update_student, name ='update-student'),
    path('update-teacher/<str:pk>/', views.update_teacher, name ='update-teacher'),
    path('student_form/', views.student_form, name='student_form'),
    path('teacher_form/', views.teacher_form, name='teacher_form')
]
