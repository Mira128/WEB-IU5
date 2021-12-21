
from django.contrib import admin
from stocks.views import GetBatonist
from stocks import views as stock_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Orchestra', stock_views.OrchesraStockViewSet)
router.register('Batonist', stock_views.BatonistStockViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('data/', GetBatonist)
]
