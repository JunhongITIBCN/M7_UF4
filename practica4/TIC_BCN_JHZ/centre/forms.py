from django.forms import ModelForm
from .models import Student, Teacher

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
