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
    #return render(request,'login.html')
def test9(request):
    return render(request,'w3.html')
def test10(request):
    return render(request,'new.html') 
def test11(request):
    return render(request,'pattern.html') 
def test12(request):
  return render(request,'pal.html') 
def test13(request):
    return render(request,'sort.html') 
def test14(request):
    return render(request,'count.html')
def test15(request):
    return render(request,'second.html')
# def test16(request):
    # return render(request,'js.html')     
def test18(request):
    return render(request,'slide.html')
def test17(request):
    return render(request,'calculator.html')
 