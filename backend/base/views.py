from django.shortcuts import render
from django.http import JsonResponse
from .models import Student, Stand
from .serializer import StudentSerializer, StandSerializer
# from django.http import HttpResponse


rooms = [
    {'id': 1, 'name': "Log In"},
    {'id': 2, 'name': "Sign Up"},
    {'id': 3, 'name': "Main"},
    {'id': 4, 'name': "Prev"},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i

    context = {'room': room}

    return render(request, 'base/room.html', context)


def student_list(request):
    students = Student.object.all()
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data)


def stand_list(request):
    stands = Stand.object.all()
    serializer = StandSerializer(stands, many=True)
    return JsonResponse(serializer.data)
