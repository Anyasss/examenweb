from rest_framework import viewsets
from blog.quickstart.serializers import  TiendaSerializer, CiudadSerializer,RegionSerializer
from blog.models import Tienda,Ciudad,Region


class TiendaViewSet(viewsets.ModelViewSet):
 
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ciudad'].queryset = Ciudad.objects.none()

        if 'region' in self.data:
                try:
                    region_id = int(self.data.get('region'))
                    self.fields['ciudad'].queryset = Ciudad.objects.filter(region_id=region_id).order_by('nombre')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty Ciudad queryset
        elif self.instance.pk:
            self.fields['ciudad'].queryset = self.instance.region.ciudad_set.order_by('nombre')


class RegionViewSet(viewsets.ModelViewSet):
 
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class CiudadViewSet(viewsets.ModelViewSet):
 
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer


