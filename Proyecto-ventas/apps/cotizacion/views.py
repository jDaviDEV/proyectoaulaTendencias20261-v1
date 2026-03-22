from django.shortcuts import render
from rest_framework import viewsets
from .models import Cotizacion
from .serializer import CotizacionSerializer
from apps.usuarios.permissions import EsVendedorOAdmin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
 
 
class CotizacionViewSet(viewsets.ModelViewSet):
 
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, EsVendedorOAdmin]