from django.db import models

class IceCreamStock(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название мороженного")
    ingridients = models.CharField(max_length=200, verbose_name="Ингридиенты в составе мороженного")
    standart = models.CharField(max_length=30, verbose_name="Стандарт мороженного")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена мороженного")
    date_modified = models.DateTimeField(auto_now=True,
                                            verbose_name="Когда последний раз обновлялась информация?")


