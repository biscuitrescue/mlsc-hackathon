from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('students/', views.student_list, name='students'),
    path('stand/', views.stand_list, name='stands')
]
