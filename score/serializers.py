from rest_framework import serializers
from .models import *

class ScoreSerializer(serializers.ModelSerializer):
    nome_jogador = serializers.CharField(source='jogador.nome')

    class Meta:
        model = Score
        fields = ['nome_jogador', 'pontos']
