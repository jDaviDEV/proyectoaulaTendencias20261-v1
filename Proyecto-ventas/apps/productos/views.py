from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializer import ProductoSerializer
from apps.usuarios.permissions import EsVendedorOAdmin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
 
 
class ProductoViewSet(viewsets.ModelViewSet):
 
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, EsVendedorOAdmin]