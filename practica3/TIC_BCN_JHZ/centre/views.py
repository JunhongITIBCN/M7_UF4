from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms  import StudentForm, TeacherForm

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def student(request):
    students = [
        {
            'id': '1',
            'nom': 'Jun',
            'cognom1': 'Zhu',
            'cognom2': 'Zhang',
            'correu': '2023_junhong.zhu@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats': ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6' , 'Mòdul 5']
        },
        {
            'id': '2',
            'nom': 'Joel',
            'cognom1': 'Ghanem',
            'cognom2': 'Gomez',
            'correu': '2023_joel.ghanem@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
            'id': '3',
            'nom': 'Anxo',
            'cognom1': 'Aragundi',
            'cognom2': 'Mesias',
            'correu': '2023_anxo.aragundi@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
            'id': '4',
            'nom': 'Eric',
            'cognom1': 'Sanchez',
            'cognom2': 'Vasquez',
            'correu': '2023_eric.sanchez@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
            'id': '5',
            'nom': 'Dinar',
            'cognom1': 'Khazimullin',
            'cognom2': 'notiene',
            'correu': '2023_dinar.khazimullin@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
            'id': '6',
            'nom': 'Carlos',
            'cognom1': 'Zambrano',
            'cognom2': 'aray',
            'correu': '2023_carlos.zambrano@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        }
    ]
    
    template = loader.get_template('alumn.html')
    return HttpResponse(template.render({'students': students}, request))


def teacher(request):
    teachers = [
        {
            'id': '1',
            'nom': 'Roger',
            'cognom': 'Sobrino',
            'edat': 39,
            'rol': 'teacher',
            'curs': ['DAM2B', 'DAW2A']
        },
        {
            'id': '2',
            'nom': 'Josep Oriol',
            'cognom': 'Roca',
            'edat': 25,
            'rol': 'teacher',
            'curs': ['DAM2B', 'DAW2A', 'DAW1A']
        },
        {
            'id': '3',
            'nom': 'Juanma',
            'cognom': 'Sanchez',
            'edat': 24,
            'rol': 'teacher',
            'curs': ['DAM2B', 'DAW2A']
        }
    ]
    template = loader.get_template('prof.html')
    return HttpResponse(template.render({'teachers': teachers}, request))


def teachers(request, pk):
    teachers = [
        {
            'id': '1',
            'nom': 'Roger',
            'cognom': 'Sobrino',
            'edat': 39,
            'rol': 'teacher',
            'curs': ['DAM2B', 'DAW2A']
        },
        {
            'id': '2',
            'nom': 'Josep Oriol',
            'cognom': 'Roca',
            'edat': 25,
            'rol': 'teacher',
            'curs': ['DAM2B', 'DAW2A', 'DAW1A']
        },
        {
            'id': '3',
            'nom': 'Juanma',
            'cognom': 'Sanchez',
            'edat': 24,
            'rol': 'teacher',
            'curs': ['DAM2B', 'DAW2A']
        }
    ]
    teachers_Obj = None
    for i in teachers :
        if i['id'] == pk:
            teachers_Obj = i
            return render(request, 'teacher.html', {'teacher': teachers_Obj})



def students(request, pk):
    students = [
        {
            'id': '1',
            'nom': 'Jun',
            'cognom1': 'Zhu',
            'cognom2': 'Zhang',
            'correu': '2023_junhong.zhu@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats': ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6' , 'Mòdul 5']
        },
        {
            'id': '2',
            'nom': 'Joel',
            'cognom1': 'Ghanem',
            'cognom2': 'Gomez',
            'correu': '2023_joel.ghanem@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
            'id': '3',
            'nom': 'Anxo',
            'cognom1': 'Aragundi',
            'cognom2': 'Mesias',
            'correu': '2023_anxo.aragundi@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
            'id': '4',
            'nom': 'Eric',
            'cognom1': 'Sanchez',
            'cognom2': 'Vasquez',
            'correu': '2023_eric.sanchez@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
            'id': '5',
            'nom': 'Dinar',
            'cognom1': 'Khazimullin',
            'cognom2': 'notiene',
            'correu': '2023_dinar.khazimullin@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
            'id': '6',
            'nom': 'Carlos',
            'cognom1': 'Zambrano',
            'cognom2': 'aray',
            'correu': '2023_carlos.zambrano@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        }
    ]
    students_Obj = None
    for i in students :
        if i['id'] == pk:
            students_Obj = i
    return render(request, 'student.html', {'student': students_Obj})

def student_form(request):
    form = StudentForm()
    context = {'form':form}
    return render(request,'form.html',context)

def teacher_form(request):
    form = TeacherForm()
    context = {'form':form}
    return render(request,'form.html',context)