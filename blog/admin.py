from django.contrib import admin
from .models import Producto,Tienda,Lista


# Register your models here.
admin.site.register(Tienda)

admin.site.register(Producto)
admin.site.register(Lista)
