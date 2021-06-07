from django.urls import path
from django.conf.urls import url
from . import views
from . import models

urlpatterns = [
    path('', views.loginregister, name='loginregister'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('home', views.index, name='index'),
    path('viewresult',views.viewresult, name='viewresult')
]