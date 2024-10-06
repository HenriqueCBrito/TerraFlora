from django.db import models

class Fazenda(models.Model):
   
    nome_proprietario = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    nome_fazenda = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=255)
    area_uso = models.DecimalField(max_digits=10, decimal_places=2)  # aq pode ter até 10 dígitos, com 2 casas decimais

 
    def __str__(self):
        return self.nome_fazenda
