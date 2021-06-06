from rest_framework import routers
from django.urls import path, include
from .views import *
from django.conf.urls import url,include

router=routers.DefaultRouter()
router.register('Comentarios',ComentarioViewSet)
router.register('Estrellas',EstrellaViewSet)

urlpatterns=[
    path('',current_datetime),
    path('api/',include(router.urls)),
    ]