from django.urls import path
from Inventory import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('displayTrucks', views.displayTrucks, name='displayTrucks'),
    path('addTrucks', views.addTrucks, name='addTrucks'),
    path('editTrucks/<int:pk>', views.editTrucks, name='editTrucks'),
    path('deleteTrucks/<int:pk>', views.deleteTrucks, name='deleteTrucks'),

    path('displaySmallVehicles', views.displaySmallVehicles, name='displaySmallVehicles'),
    path('addSmallVehicles', views.addSmallVehicles, name='addSmallVehicles'),
    path('editSmallVehicles/<int:pk>', views.editSmallVehicles, name='editSmallVehicles'),
    path('deleteSmallVehicles/<int:pk>', views.deleteSmallVehicles, name='deleteSmallVehicles'),

    path('TruckDetailView/<int:pk>', views.TruckDetailView, name='truckdetails'),
    path('VehicleDetails/<int:pk>', views.VehicleDetailView, name='vehicledetails'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)