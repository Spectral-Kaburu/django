from django.urls import path
from . import views

#URLConf
urlpatterns = [   # very important
    path('hello/', views.say_hello)
]