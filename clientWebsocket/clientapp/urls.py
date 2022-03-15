from django.urls import path, include
from . import views


urlpatterns = [
    path('ct/', views.CTest,name='CTEST'),
    path('signup/', views.Signup,name='SIGNUP'),
    path('login/', views.Login,name='LOGIN'),
    path('', views.Index,name='INDEX'),
    
    path('logout/',views.ClientLogOut,name='LOGOUT'),
]