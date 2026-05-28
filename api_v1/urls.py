from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, BrandViewSet, LaptopViewSet, RepairViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'laptops', LaptopViewSet, basename='laptop')
router.register(r'repairs', RepairViewSet, basename='repair')

urlpatterns = [
    path('', include(router.urls)),
]