from django.db import models
from django.contrib.auth.models import User


class Program(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="program-img")
    description = models.TextField()
    venue = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name