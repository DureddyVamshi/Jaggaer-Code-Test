from django.db import models

class UserModel(models.Model):

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username