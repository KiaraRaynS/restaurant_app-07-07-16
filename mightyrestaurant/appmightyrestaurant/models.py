from django.db import models

typechoices = (
        ('owner', 'Owner'),
        ('cook', 'Cook'),
        ('server', 'Server'),
        )


class Worker(models.Model):
    name = models.CharField(max_length=40)
    workertype = models.CharField(max_length=10, choices=typechoices)
    hirement = models.DateTimeField(auto_now_add=True)


class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    foodtype = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
