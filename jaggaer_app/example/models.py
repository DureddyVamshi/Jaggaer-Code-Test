from django.db import models

class CustomUserModel(models.Model):

    USER_TYPE_CHOICES = (
        ('djangoadmin', 'DjangoAdmin'),
        ('user', 'User')
    )


    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    organization = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username

class OrganizationModel(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name