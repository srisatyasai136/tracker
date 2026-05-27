from django.db import models

class Location(models.Model):
 latitude=models.CharField(max_length=50)
 longitude=models.CharField(max_length=50)
 time=models.CharField(max_length=100)
 created=models.DateTimeField(auto_now_add=True)