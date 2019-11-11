from django.db import models
from django.conf import settings

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=500, default='Note')
    note_text=models.CharField(max_length=500)
    moment=models.DateTimeField()
    


