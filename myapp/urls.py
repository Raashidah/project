
from django.urls import path,include
from . import views

urlpatterns = [
    path('test',views.test1,name='test'),
    path('app',views.test2,name='app'),
    path('index',views.test3,name='index'),
    path('head',views.test4,name='head'),
    path('clg',views.test5,name='clg'),
    path('login',views.test6,name='login')

]