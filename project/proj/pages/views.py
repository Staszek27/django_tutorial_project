from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs):
    my_context = {
        'my_text' : 'this is about me',
        'number' : 123
    }
    return render(request, 'home.html', my_context)