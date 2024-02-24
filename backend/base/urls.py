from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('students/', views.student_list, name='students'),
    path('stand/', views.stand_list, name='stands'),
    path('students/<int:id>', views.student_deets, name='students_deets'),
    path('stand/<int:id>', views.stand_deets, name='stands_deets'),
]

