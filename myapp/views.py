from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test1(request):
    return HttpResponse("hello world") 
def test3(request):
    return render(request,'index.html')
def test4(request):
    return render(request,'head.html') 
def test5(request):
    return render(request,'college.html')       
def test7(request):
    return render(request,'anim.html') 
def test8(request):
    return render(request,'facebook.html')     
#def test6(request):
  #  return render(request,'login.html')
def test9(request):
    return render(request,'w3.html')     
def test10(request):
    return render(request,'new.html')       