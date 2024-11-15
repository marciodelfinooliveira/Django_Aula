from django.db import models

class Cep(models.Model):
    
    cep =  models.CharField(max_length=9)
    uf = models.CharField(max_length=2)
    ddd = models.CharField(max_length=2)
    cidade = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    rua = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.cep

     