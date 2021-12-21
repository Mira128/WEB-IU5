from django.shortcuts import render
from rest_framework import viewsets
from stocks.serializers import OrchesraStockSerializer, BatonistStockSerializer
from stocks.models import OrchesraStock, BatonistStock

class OrchesraStockViewSet(viewsets.ModelViewSet):
    queryset = OrchesraStock.objects.all().order_by('pk')
    serializer_class = OrchesraStockSerializer

class BatonistStockViewSet(viewsets.ModelViewSet):
    queryset = BatonistStock.objects.all().order_by('pk')
    serializer_class = BatonistStockSerializer

def GetBatonist(request):
    context={
        'data':BatonistStock.objects.select_related('idOrch') }
    return render (request,'orchesras.html',context)