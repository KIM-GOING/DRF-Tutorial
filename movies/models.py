from django.db import models

class Movie(models.Model) :
    name = models.CharField(max_length=30)
    opening_date = models.DateField(default='')
    running_time = models.IntegerField(default=0)
    overview = models.TextField()