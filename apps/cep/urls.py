# from django.urls import path
# from apps.cep.api.viewsets import CepViewSet, ShowCepList


# urlpatterns=[
    
#     path('cep/<str:cep>/', CepViewSet.as_view(), name='cep-view'),
#     path('show/', ShowCepList.as_view(), name='cep-models')
# ]

from django.urls import path, include
from apps.cep.api.viewsets import CepViewSet, ShowCepList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cep', CepViewSet, basename='Cep')
router.register(r'show', ShowCepList, basename='ShowCepList')

urlpatterns = [
    path("api/", include(router.urls)),
]