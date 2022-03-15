from django.urls import path, include
from . import views

urlpatterns = [
    path('st/', views.STest,name='STEST'),

]