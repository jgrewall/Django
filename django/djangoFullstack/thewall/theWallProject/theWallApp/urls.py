from django.urls import path
from . import views

urlpatterns =[
    #display
    path('', views.index),
    path('success', views.displaysuccess),

    #redirect
    path('newUser', views.newUser),
    path('login', views.login),
    path('logout', views.logout),

    path('comment', views.comment),
    path('message', views.message)

]