from django.db import models
class ToDo(models.Model):
	question = models.CharField(max_length=200)
	finished = models.BooleanField()
# Create your models here.
