from django.db import models

# Create your models here.

class Books(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    autor = models.CharField(max_length=100, null=False)
    editora = models.CharField(max_length=100, null=False)
    ano_publicacao = models.IntegerField()
    resumo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
