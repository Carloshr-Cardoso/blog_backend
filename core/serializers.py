from rest_framework import serializers
from .models import Postagem

# Serializers define the API representation.
class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = ['id', 'tag', 'title', 'content']