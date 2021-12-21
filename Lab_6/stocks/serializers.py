from stocks.models import IceCreamStock
from rest_framework import serializers


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = IceCreamStock
        # Поля, которые мы сериализуем
        fields = ["pk", "title", "ingridients", "standart", "price", "date_modified"]
