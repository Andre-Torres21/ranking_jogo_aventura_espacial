from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Jogadores'
        
    def __str__(self):
        return self.nome

class Score(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    pontos = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.jogador} - Pontos: {self.pontos}"