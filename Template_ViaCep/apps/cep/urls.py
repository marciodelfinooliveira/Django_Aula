from django.urls import path
from apps.cep.api.viewsets import CepViewSet, ShowCepList


urlpatterns=[
    
    path('cep/<str:cep>/', CepViewSet.as_view(), name='cep-view'),
    path('show/', ShowCepList.as_view(), name='cep-models')
]