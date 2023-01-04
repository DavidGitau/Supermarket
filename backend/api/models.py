from django.db import models

# Create your models here.

class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    STAFF_CHOICES = (
        ('A', 'Admin'),
        ('S', 'Staff'),
    )
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    level = models.CharField(max_length=1, choices=STAFF_CHOICES)
    uid = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

