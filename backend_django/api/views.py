from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import datetime
from django.http import HttpResponse

# Create your views here.
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset= Comentario.objects.all()
    serializer_class=SerializerComentario

class EstrellaViewSet(viewsets.ModelViewSet):
    queryset= Estrella.objects.all()
    serializer_class=SerializerEstrella

def current_datetime(request):
    now = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    html = "<html><body><p style = 'text-align:center; margin-top:auto;margin-bottom:auto'>Tiempo en Ecuador: %s.</p><div style='text-align:center'><a href='http://localhost:8000/api'>Visitar api</a><br/><a href='http://localhost:8000/admin'>Visitar pagina de administración en django</a></div></body></html>" % now
    return HttpResponse(html)