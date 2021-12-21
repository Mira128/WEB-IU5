from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class IceCream(models.Model):
    title = models.CharField(max_length=30)
    ingridients = models.CharField(max_length=200)
    standart = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    idtype = models.ForeignKey('Icecreamtype', models.DO_NOTHING, db_column='idType')

    class Meta:
        managed = False
        db_table = 'IceCream'

class IceCreamType(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'IceCreamType'