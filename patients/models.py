from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # owner
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    condition = models.TextField()

    def __str__(self):
        return self.name
