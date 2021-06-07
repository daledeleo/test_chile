from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import datetime
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["DELETE"]) ##api/clientes/
def delete_all_comentarios(request):
    if request.method == 'DELETE':
        comentarios = Comentario.objects.all().delete()
        return Response(data="Exito al eliminar todas las opiniones.", status=status.HTTP_200_OK)

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset= Comentario.objects.all()
    serializer_class=SerializerComentario

    def destroy(self, request):
        Comentario.objects.all().delete()
        return Response(data="Exito en borrar todas las opniones", status=status.HTTP_200_OK)

class EstrellaViewSet(viewsets.ModelViewSet):
    queryset= Estrella.objects.all()
    serializer_class=SerializerEstrella

def current_datetime(request):
    now = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    html = "<html><body><p style = 'text-align:center; margin-top:auto;margin-bottom:auto'>Tiempo en Ecuador: %s.</p><div style='text-align:center'><a href='https://backend-chile-test.herokuapp.com/api'>Visitar api</a><br/><a href='https://backend-chile-test.herokuapp.com/admin'>Visitar pagina de administración en django</a></div></body></html>" % now
    return HttpResponse(html)
