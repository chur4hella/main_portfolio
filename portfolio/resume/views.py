from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'resume/index.html')

def about(request):
    return render(request, 'resume/about.html')

def skills(request):
    return render(request, 'resume/skills.html')

def works(request):
    return render(request, 'resume/works.html')

def contact(request):
    return render(request, 'resume/contact.html')