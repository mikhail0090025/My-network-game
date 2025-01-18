from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    path_to_avatar = models.CharField(max_length=400)
    registration_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
