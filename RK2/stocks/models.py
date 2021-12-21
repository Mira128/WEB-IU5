from django.db import models
from django.utils.datetime_safe import datetime


class OrchesraStock(models.Model):
    nameOrch = models.CharField(max_length=50, verbose_name="Название оркестра")
    membersNum = models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Количество участников")
    dateCreation = models.DateTimeField(verbose_name="Дата формирования")

class BatonistStock(models.Model):
    nameBat = models.CharField(max_length=30, verbose_name="Имя дирижера")
    secondName = models.CharField(max_length=200, verbose_name="Фамилия дирижера")
    age = models.DecimalField(max_digits=3, decimal_places=0, verbose_name="Возраст дирижера")
    experience = models.DecimalField(max_digits=3, decimal_places=0, verbose_name="Стаж дирижера")
    idOrch = models.ForeignKey('OrchesraStock', models.DO_NOTHING, db_column='idOrch')
