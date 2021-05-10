from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test1(request):
    return HttpResponse("hello world")
def test2(request):
    return HttpResponse("<H1>HIIIIIIIII</H1>") 
def test3(request):
    return render(request,'index.html')
def test4(request):
    return render(request,'head.html')    