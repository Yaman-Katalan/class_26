from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.

class Pet(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=60, blank=False, null=False)
    des = models.TextField(max_length=200)
    breed = models.CharField(max_length=60)
    birth_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name