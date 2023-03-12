from django.urls import path

from . import views

urlpatterns = [
    path('programming-languages', views.index, name='index'),
]