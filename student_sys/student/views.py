from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Student
from .forms import StudentForm

def index(request):
    # students = Student.objects.all()
    # words = 'World!'
    # return render(request, 'index.html', context={'students': students})
    students = Student.get_all()    # 获取学生信息，此处用函数调取，get_all()方法在models.py 中

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_vaild():
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        form = StudentForm()

    context = {
        'students': students,
        'forms': form,

    }
    return render(request, 'index.html', context=context)





