from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def load(request):
    task=request.POST['task']
    priority=request.POST['priority']
    return HttpResponse("hello")