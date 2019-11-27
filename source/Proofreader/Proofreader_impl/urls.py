from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Landing,name='Landing'),
    path('index',views.index,name='index'),
    path('register',views.Register,name="Register"),
    path('logout',views.logout_view,name="logout_view")
]
