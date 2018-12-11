from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import Tienda,Ciudad,Region


class TiendaSerializer(serializers.HyperlinkedModelSerializer):
    
    
    class Meta:
        model = Tienda
        fields = ('nombre','sucursal','direccion','region','ciudad')
          


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('id','nombre')

class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = Ciudad
        fields = ('id','nombre','region_id')







   
