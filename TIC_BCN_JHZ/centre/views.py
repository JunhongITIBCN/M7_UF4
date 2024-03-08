from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def student(request):
    from django.shortcuts import render

def students(request):
    alumnos = [
        {
            'id': 1,
            'nom': 'Juan',
            'cognom1': 'García',
            'cognom2': 'Pérez',
            'correu': 'juan@example.com',
            'curs': 'DAW2B',
            'moduls_matriculats': ['Mòdul A', 'Mòdul B']
        },
        {
            'nom': 'María',
            'cognom1': 'Martínez',
            'cognom2': 'López',
            'correu': 'maria@example.com',
            'curs': 'DAW2B',
            'moduls_matriculats': ['Mòdul C', 'Mòdul D']
        },
        
    ]
    
    return render(request, 'centre/students.html', {'alumnos': alumnos})


def teacher(request):
    teachers = [
        {
            'id' : '1',
            'nom' : 'Roger',
            'cognom' : 'Sobrino',
            'edat' : 39,
            'rol' : 'teacher',
            'curs' : ['DAM2B', 'DAW2A']
        },
        {
            'id' : '2',
            'nom' : 'Josep Oriol',
            'cognom' : 'Roca',
            'edat' : 25,
            'rol' : 'teacher',
            'curs' : ['DAM2B', 'DAW2A', 'DAW1A']
        },
        {
            'id' : '3',
            'nom' : 'Juanma',
            'cognom' : 'Sanchez',
            'edat' : 24,
            'rol' : 'teacher',
            'curs' : ['DAM2B', 'DAW2A']
        }

    ]
    return  render(request, 'centre/prof.html', {'teachers': teachers})

# Create your views here.
