from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)

class Family(models.Model):
    member = models.ForeignKey(Person, on_delete=models.CASCADE)

class Item(models.Model):
    itemName = models.CharField(max_length=200)
    needBuy = models.BooleanField(default=True)
    date = models.DateTimeField('date published')
    createdBy = models.ForeignKey(Person, on_delete=models.CASCADE)
