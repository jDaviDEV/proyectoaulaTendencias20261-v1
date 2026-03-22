from rest_framework import serializers
from .models import Cotizacion, ItemCotizacion
 
 
class ItemCotizacionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ItemCotizacion
        fields = ['producto', 'cantidad']
 
 
class CotizacionSerializer(serializers.ModelSerializer):
 
    items = ItemCotizacionSerializer(many=True)
 
    class Meta:
        model = Cotizacion
        fields = "__all__"
 
    def create(self, validated_data):
 
        items_data = validated_data.pop('items')
        cotizacion = Cotizacion.objects.create(**validated_data)
 
        for item_data in items_data:
            ItemCotizacion.objects.create(
                cotizacion=cotizacion,
                **item_data
            )
 
        return cotizacion