from django.shortcuts import render

from .models import Student

def index(request):
    students = Student.objects.all()
    # words = 'World!'
    # return render(request, 'index.html', context={'students': students})

    if request.method == 'POST':
        form = StudentForm(request.POST)

