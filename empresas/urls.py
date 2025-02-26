from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import EmpresaViewSet


router = DefaultRouter()
router.register('empresas', EmpresaViewSet)


urlpatterns = router.urls