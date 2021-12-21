from django.contrib import admin
from django.urls import path

from lab_5_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetIcecreams, name='home_url'),
    path('icecream/<int:pk>', views.GetIcecream, name='icecream_url'),
]
