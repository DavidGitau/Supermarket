from django.db import models

class Common(models.Model):    
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Category(Common):
    pass 

class Order(models.Model):
    order_id = models.IntegerField()
    items = models.ManyToManyField('Product')
    amount = models.FloatField()

class Product(Common):
    price = models.FloatField()
    number = models.IntegerField()
    description = models.TextField(null=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

class User(Common):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    STAFF_CHOICES = (
        ('A', 'Admin'),
        ('S', 'Staff'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    level = models.CharField(max_length=1, choices=STAFF_CHOICES)
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=100)