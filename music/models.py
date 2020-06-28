from django.db import models

# Create your models here.
class Song(models.Model):
    title=models.CharField(max_length=20)
    singer=models.CharField(max_length=20)

    def __str__(self):
        return self.title
