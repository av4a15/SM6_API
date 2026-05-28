from rest_framework import serializers
from .models import Client, Brand, Laptop, Repair


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'phone']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class LaptopSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), source='brand', write_only=True
    )
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), source='client', write_only=True
    )

    class Meta:
        model = Laptop
        fields = [
            'id', 'brand', 'brand_id', 'model', 'serial_number',
            'client', 'client_id', 'published_date', 'issue_description',
            'received_date', 'created_at'
        ]


class RepairSerializer(serializers.ModelSerializer):
    laptop = serializers.StringRelatedField(read_only=True)
    laptop_id = serializers.PrimaryKeyRelatedField(
        queryset=Laptop.objects.all(), source='laptop', write_only=True
    )

    class Meta:
        model = Repair
        fields = ['id', 'laptop', 'laptop_id', 'diagnosis', 'cost', 'created_at']