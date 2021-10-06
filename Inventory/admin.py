from django.contrib import admin
from .models import trucks, smallVehicles


@admin.register(trucks, smallVehicles)
class DefaultAdmin(admin.ModelAdmin):
    pass