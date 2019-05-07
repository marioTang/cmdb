
from django.contrib import admin
from django.urls import path
from web import views
urlpatterns = [
    path('index/', views.index),
    path('host/', views.getall),
    path('login/', views.login),
    path('register/', views.register),
    path('users/', views.users),
    path('deluser/', views.deluser),
    path('edituser/', views.edituser),
    path('edituserdata/', views.edituser),
    path('logout/', views.logouts),
]

