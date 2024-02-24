from django.shortcuts import render
from django.http import JsonResponse
from .models import Student, Stand
from .serializer import StudentSerializer, StandSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
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


@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
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


@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
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


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([permissions.AllowAny])
def student_deets(request, id):

    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    # elif request.method == 'PUT':
    #     pass
    # elif request.method == 'DELETE':
    #     pass


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.AllowAny])
def stand_deets(request, id):

    try:
        stand = Stand.objects.get(pk=id)
    except Stand.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StandSerializer(stand)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StandSerializer(stand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        stand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
