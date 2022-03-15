from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.CTest,name='CTEST'),
    path('signup/', views.Signup,name='SIGNUP'),
    path('login/', views.Login,name='LOGIN'),

]