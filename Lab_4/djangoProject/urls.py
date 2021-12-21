
from django.contrib import admin
from django.urls import path
from Lab_4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetIcecreams, name='home_url'),
    path('details/<int:id>', views.GetIcecream, name='icecream_url'),
]
