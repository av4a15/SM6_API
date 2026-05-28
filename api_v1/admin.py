from django.contrib import admin
from .models import Client, Brand, Laptop, Repair


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    search_fields = ['name', 'phone']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'serial_number', 'client', 'received_date', 'created_at']
    search_fields = ['serial_number', 'model']
    list_filter = ['brand', 'received_date']


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ['id', 'laptop', 'diagnosis', 'cost', 'created_at']
    search_fields = ['diagnosis']