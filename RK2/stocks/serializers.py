from stocks.models import OrchesraStock, BatonistStock
from rest_framework import serializers


class OrchesraStockSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = OrchesraStock
        # Поля, которые мы сериализуем
        fields = ["pk", "nameOrch", "membersNum", "dateCreation"]

class BatonistStockSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = BatonistStock
        # Поля, которые мы сериализуем
        fields = ["pk", "nameBat", "secondName", "age", "experience", "idOrch"]