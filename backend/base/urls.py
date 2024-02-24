from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('students/', views.student_list, name='students'),
    path('stand/', views.stand_list, name='stands'),
    path('students/<int:id>', views.student_deets, name='students_deets'),
    path('stand/<int:id>', views.stand_deets, name='stands_deets'),
]
urlpattern= format_suffix_patterns(urlpatterns)