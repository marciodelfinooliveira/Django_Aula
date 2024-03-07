from apps.cep.models import Cep
from rest_framework import serializers

class CepSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cep
        fields = ['cep', 'rua', 'bairro', 'cidade', 'uf', 'ddd']
