from django.db import models

# Create your models here.

class Equipamento(models.Model):
    id_equipamento = models.IntegerField
    local = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='equipamentos/', null=True, blank=True)

    def __str__(self):
        return self.id