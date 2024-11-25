from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import ScoreSerializer

@api_view(['POST'])
def salvar_score(request):
    nome = request.data.get('nome_jogador')
    pontos = request.data.get('score')
    jogador, _ = Jogador.objects.get_or_create(nome=nome)
    score = Score.objects.create(jogador=jogador, pontos=pontos)
    return Response({"message": "Score salvo com sucesso!", "id": score.id})

@api_view(['GET'])
def rankings(request):
    scores = Score.objects.order_by('-pontos')
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)
