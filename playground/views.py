from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    # return HttpResponse('<h1>Hello World</h1>')
    x = 2
    y = 4
    return render(request, 'hello.html', {'name':''})
