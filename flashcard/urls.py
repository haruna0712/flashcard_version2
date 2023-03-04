# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:42:22 2023

@author: haruna
"""
from django.urls import path
from . import views

app_name='flashcard'

urlpatterns = [
    path('index/',views.IndexView,name='index'),
    path('flashcard/create/', views.FlashcardCreateView, name='flashcard_create'),
    path('edit/<int:num>/',views.edit,name='edit'),
    path('delete/<int:num>/',views.delete,name='delete'),
    path('index/list/', views.find, name='flashcard_list'),
    path('index/list/<int:num>/',views.find, name='flashcard_list' ),
    path("login/",views.LoginView.as_view(),name="login"),
    path('index/test/',views.test_Indexview.as_view(),name='myIndex'),
    path('detail/<int:pk>/',views.DetailView.as_view(),name='detail'),
];