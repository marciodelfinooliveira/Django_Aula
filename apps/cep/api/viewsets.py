from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import requests
from apps.cep.models import Cep
from .serializers import CepSerializer
class CepViewSet(ModelViewSet):
    
    queryset = Cep.objects.all()
    serializer_class = CepSerializer

    def create(self, request):
        
        dados = request.data
        cep = dados['cep']

        url = f'https://viacep.com.br/ws/{cep}/json/'
        
        resposta = requests.get(url)
        dados_cep = resposta.json()

        este_cep = dados_cep.get('cep', '')

        objeto_cep_plmrds = Cep.objects.filter(cep=este_cep)

        if objeto_cep_plmrds.exists():
            return Response({"error": "CEP já cadastrado"}, status=400)
        else:

            serializer = CepSerializer(data={
                'cep': dados_cep.get('cep', ''),
                'rua': dados_cep.get('logradouro', ''),
                'bairro': dados_cep.get('bairro', ''),
                'cidade': dados_cep.get('localidade', ''),
                'uf': dados_cep.get('uf', ''),
                'ddd': dados_cep.get('ddd', ''),
            })

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=400)
        
class ShowCepList(ModelViewSet):
    
    queryset = Cep.objects.all()
    serializer_class = CepSerializer

    def list(self, request):
        queryset = Cep.objects.all()
        serializer = CepSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    
        
        
        
        
        
