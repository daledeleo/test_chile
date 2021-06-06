from rest_framework import serializers
from .models import *


class SerializerEstrella(serializers.ModelSerializer):
    class Meta:
        model = Estrella
        fields = "__all__"

class SerializerComentario(serializers.ModelSerializer):
    class Meta:
        model=Comentario
        fields='__all__'

    def to_representation(self, instance):
        self.fields['id_estrella'] =  SerializerEstrella(read_only=True)
        return super(SerializerComentario, self).to_representation(instance)

