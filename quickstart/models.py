from django.db import models


class Student(models.Model):
    name = models.CharField(null=False)
    age = models.IntegerField()
