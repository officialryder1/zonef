from django.shortcuts import render
from .models import Program

def home(request):
    program = Program.objects.all()
    content = {
        'program':program
    }
    return render(request, 'zonef/index.html', content)