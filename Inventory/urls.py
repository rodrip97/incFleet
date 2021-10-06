
from django.urls import path
from Inventory import views


urlpatterns = [
    path('displayTrucks', views.displayTrucks, name='displayTrucks'),
    path('addTrucks', views.addTrucks, name='addTrucks'),


    path('displaySmallVehicles', views.displaySmallVehicles, name='displaySmallVehicles'),
    path('addSmallVehicles', views.addSmallVehicles, name='addSmallVehicle'),

]
