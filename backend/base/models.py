from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.CharField(max_length=9)
    location = models.CharField(max_length=50)


class Stand(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
