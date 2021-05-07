from django.urls import path 
from . import views

urlpatterns=[path('', views.index),
path("offers",views.index1),
path("login",views.login),
path("register",views.register)
]