from django.db import models

class Student(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100)
    correu = models.EmailField()
    curs = models.CharField(max_length=10)
    moduls_matriculats = models.TextField()

class Teacher(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    edat = models.PositiveIntegerField()
    rol = models.CharField(max_length=100)
    curs = models.TextField()
