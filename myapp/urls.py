
from django.urls import path,include
from . import views

urlpatterns = [
    path('test',views.test1,name='test'),
    path('index',views.test3,name='index'),
    path('head',views.test4,name='head'),
    path('clg',views.test5,name='clg'),
   # path('login',views.test6,name='login'),
    path('slide',views.test7,name='slide'),
    path('fb',views.test8,name='fb'),
    path('w3',views.test9,name='w3'),
    path('new',views.test10,name='new'),
    path('pattern',views.test11,name='pattern'),
    path('pal',views.test12,name='pallindrome'),
    path('sort',views.test13,name='sort'),
    path('count',views.test14,name='count'),
    path('second',views.test15,name='second'),
    # path('js',views.test16,name='js'),
    path('slider',views.test18,name='slider'),
    path('calc',views.test17,name='calc'),
   
    

]