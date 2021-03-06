from django.shortcuts import render
from rest_framework import viewsets
from .models import Postagem
from .serializers import PostagemSerializer

# Create your views here.
# ViewSets define the view behavior.
class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer