from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Doggie Is Good!'}
    return render(request, 'doggie/index.html', context=context_dict)

def about(request):
    return render(request, 'doggie/about.html')
