from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Student, Teacher
from .forms  import StudentForm, TeacherForm
from django.shortcuts import render, redirect

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def student(request):
    students = Student.objects.all()  
    context = {'students': students}  
    return render(request, 'alumn.html', context)

def teacher(request):
    students = Teacher.objects.all()  
    context = {'teachers': students}  
    return render(request, 'prof.html', context)



def update_student(request,pk):
    student = Student.objects.get(id = pk)
    form = StudentForm(instance= student)

    if request.method == 'POST':
       form = StudentForm(request.POST, instance= student)
       if form.is_valid():
           form.save()
           return redirect('index')
    
    context = {'form' : form}
    return render(request, 'form.html', context)

def update_teacher(request,pk):
    teacher = Teacher.objects.get(id = pk)
    form = TeacherForm(instance= teacher)

    if request.method == 'POST':
       form = TeacherForm(request.POST, instance= teacher)
       if form.is_valid():
           form.save()
           return redirect('index')
    
    context = {'form' : form}
    return render(request, 'form.html', context)



def student_form(request):
    form = StudentForm()
    if request.method == 'POST':  
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    context = {'form': form}
    return render(request, 'form.html', context)

def teacher_form(request):
    form = TeacherForm()
    if request.method == 'POST':  
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    context = {'form': form}
    return render(request, 'form.html', context)

  