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
from django.shortcuts import render, get_object_or_404
from .models import Teacher

def teachers(request, pk):
    teacher_obj = get_object_or_404(Teacher, id=pk)
    context = {'teacher': teacher_obj}
    return render(request, 'teacher.html', context)



def students(request, pk):
    student_obj = get_object_or_404(Student, id=pk)
    context = {'student': student_obj}
    return render(request, 'student.html', context)

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

  