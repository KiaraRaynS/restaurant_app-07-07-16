from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

typechoices = (
        ('owner', 'Owner'),
        ('cook', 'Cook'),
        ('server', 'Server'),
        )


class Worker(models.Model):
    user = models.OneToOneField('auth.user')
    name = models.CharField(max_length=40, null=True, blank=True)
    workertype = models.CharField(max_length=10, choices=typechoices, null=True, blank=True)
    hirement = models.DateTimeField(auto_now_add=True)


class FoodType(models.Model):
    category = models.CharField(max_length=50)
    ordernumber = models.IntegerField()

    def __str__(self):
        return str(self.category)


class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    foodtype = models.ForeignKey(FoodType)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return str(self.title)


class CustomerTable(models.Model):
    partyname = models.CharField(max_length=50)


class Order(models.Model):
    tableid = models.ForeignKey(CustomerTable)
    customer = models.CharField(max_length=50)
    orderitem = models.ForeignKey(MenuItem)
    notes = models.TextField(null=True, blank=True)
    server = models.ForeignKey(Worker)
    foodstatus = models.BooleanField(default=False)
    paidstatus = models.BooleanField(default=False)


@receiver(post_save, sender='auth.user')
def create_worker_data(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
            Worker.objects.create(user=instance)
