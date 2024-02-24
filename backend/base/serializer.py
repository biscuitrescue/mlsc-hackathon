from rest_framework import serializers
from .models import Stand, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'location']


class StandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stand
        fields = ['name', 'location']
