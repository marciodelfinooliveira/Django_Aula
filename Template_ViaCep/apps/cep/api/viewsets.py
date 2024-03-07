import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.cep.models import Cep
from apps.cep.api.serializers import CepSerializer
from rest_framework.generics import ListAPIView


#https://www.4devs.com.br/gerador_de_cep

class CepViewSet(APIView):
    
    def get(self, request, cep):
        
        url = f'https://viacep.com.br/ws/{cep}/json/'
        
        response = requests.get(url)
        
        if request.method == 'GET':
                
            data = response.json()
            
            if data.get('cep') in Cep.objects.values_list('cep', flat=True):
                
                return Response({"error": "CEP já cadastrado"}, status=400)

            cep = Cep.objects.create(
                cep=data.get('cep'),
                rua=data.get('logradouro'),
                bairro=data.get('bairro'),
                cidade=data.get('localidade'),
                uf=data.get('uf'),
                ddd=data.get('ddd'),
            )

            cep.save()
            
            return Response(data)
        
        else:
            
            return Response({"error": "CEP não encontrado"}, status=response.status_code)
        
class ShowCepList(ListAPIView):
    
    queryset = Cep.objects.all()
    serializer_class = CepSerializer

    
    
    
    
    
        
        
        
        
        
