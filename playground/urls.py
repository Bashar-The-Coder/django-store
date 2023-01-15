from django.urls import path #ch-12
from .import views

#URLConf
urlpatterns = [
    path('hello/', views.say_hello, name='hello'),
]
