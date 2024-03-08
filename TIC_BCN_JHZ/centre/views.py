from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def student(request):
    from django.shortcuts import render

def students(request):
    students = [
        {
            'nom': 'Jun',
            'cognom1': 'Zhu',
            'cognom2': 'Zhang',
            'correu': '2023_junhong.zhu@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats': ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6' , 'Mòdul 5']
        },
        {
            'nom': 'Joel',
            'cognom1': 'Ghanem',
            'cognom2': 'Gomez',
            'correu': '2023_joel.ghanem@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
            'nom': 'Anxo',
            'cognom1': 'Aragundi',
            'cognom2': 'Mesias',
            'correu': '2023_anxo.aragundi@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
            'nom': 'Eric',
            'cognom1': 'Sanchez',
            'cognom2': 'Vasquez',
            'correu': '2023_eric.sanchez@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
            'nom': 'Dinar',
            'cognom1': 'Khazimullin',
            'cognom2': 'notiene',
            'correu': '2023_dinar.khazimullin@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls_matriculats':  ['Mòdul 9', 'Mòdul 7' , 'Mòdul 6']
        },
        {
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

# Create your views here.
