from django.db import models


class Avatar(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='avatar_media')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date_added)
    
class Thumbnail(models.Model):
    event = models.CharField(max_length=100)
    image = models.ImageField(upload_to="thumbnail")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event
    
class Result(models.Model):
    image = models.ImageField(upload_to="result")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date_added)


