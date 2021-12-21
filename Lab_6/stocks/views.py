from rest_framework import viewsets
from stocks.serializers import StockSerializer
from stocks.models import IceCreamStock


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по primary key
    queryset = IceCreamStock.objects.all().order_by('pk')
    serializer_class = StockSerializer  # Сериализатор для модели
