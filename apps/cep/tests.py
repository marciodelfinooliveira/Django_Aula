from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.cep.models import Cep
from unittest.mock import patch

class TestCepViewSet(APITestCase):
    
    # Cria um CEP inicial para teste
    def setUp(self):
        self.cep = Cep.objects.create(
            cep="58053002",
            rua="Rodovia BR-230",
            bairro="Água Fria",
            cidade="João Pessoa",
            uf="PB",
            ddd="83"
        )
        self.valid_cep_data = {
            "cep": "58043320"
        }
        self.invalid_cep_data = {
            "cep": "00000000"
        }
        
    @patch('apps.cep.api.viewsets.requests.get')
    def test_create_cep_valido(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "cep": "58043320",
            "logradouro": "Rua Marieta Steimbach Silva",
            "bairro": "Miramar",
            "localidade": "João Pessoa",
            "uf": "PB",
            "ddd": "83"
        }
        
        url = reverse('cep-list') 
        response = self.client.post(url, self.valid_cep_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('cep', response.data)

    @patch('apps.cep.api.viewsets.requests.get')
    def test_create_cep_duplicado(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "cep": "58053002",
            "logradouro": "Rodovia BR-230",
            "bairro": "Água Fria",
            "localidade": "João Pessoa",
            "uf": "PB",
            "ddd": "83"
        }
        
        url = reverse('cep-list')
        response = self.client.post(url, {"cep": "58053002"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "CEP já cadastrado")

    # Testa CEP inválido
    @patch('apps.cep.api.viewsets.requests.get')
    def test_create_cep_invalido(self, mock_get):
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {
            "erro": "true"
        }
        
        url = reverse('cep-list')
        response = self.client.post(url, self.invalid_cep_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('cep', response.data)

    # Teste para listar todos os CEPs
    def test_list_ceps(self):
        url = reverse('cep-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # Teste para buscar um CEP específico
    def test_retrieve_cep(self):
        url = reverse('cep-detail', args=[self.cep.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cep'], self.cep.cep)

    # Teste para deletar um CEP existente
    def test_delete_cep(self):
        url = reverse('cep-detail', args=[self.cep.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Cep.objects.filter(id=self.cep.id).exists())
