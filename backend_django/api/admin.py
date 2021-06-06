from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Estrella)
class EstrellaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombres","apellidos")
    search_fields = ["nombres", "apellidos"]
    list_filter = ["id"]

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nickname","comentario", "valoracion", "id_estrella")
    search_fields = ["nickname", "valoracion"]
    list_filter = ["id"]