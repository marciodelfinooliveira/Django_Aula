from django.urls import path, include 
from apps.cep.api.viewsets import CepViewSet, ShowCepList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cep', CepViewSet, basename='cep')
router.register(r'show', ShowCepList, basename='show')

urlpatterns = [
    path("api/", include(router.urls)),
]
