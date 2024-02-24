from django.shortcuts import render
from django.http import JsonResponse
from .models import Student, Stand
from .serializer import StudentSerializer, StandSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from django.http import HttpResponse


rooms = [
    {'id': 1, 'name': "Log In"},
    {'id': 2, 'name': "Sign Up"},
    {'id': 3, 'name': "Main"},
    {'id': 4, 'name': "Prev"},
    {'id': 5, 'name': "Wallet"},
    {'id': 6, 'name': "Feedback"},
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


# @api_view(['GET', 'POST'])
def student_list(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


def stand_list(request):

    if request.method == 'GET':
        stands = Stand.objects.all()
        serializer = StandSerializer(stands, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = StandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# def student_deets():
#     pass
