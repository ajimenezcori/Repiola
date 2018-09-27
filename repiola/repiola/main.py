from django.http import HttpResponse

from django.shortcuts import render

def __main__(request):
    return render(request, 'index.html')
    
