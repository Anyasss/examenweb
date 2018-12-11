from django.conf.urls import include, url
from . import views
from django.urls import include, path
from .views import ListadoCompras,CrearCompra,ModificarCompra
from django.views.generic import TemplateView


app_name ='blog'

urlpatterns = [
    url(r'^$', views.main,name='home'),
    url(r'^registro$', views.registro,name='registro'),
    path('ajax/load-cities/', views.load_ciudades, name='load_ciudades'),
    url(r'^producto$', views.producto,name='producto'),
    url(r'^producto/(?P<pk>[0-9]+)/$', views.producto_detail, name='producto_detail'),
    url(r'^modificar_compra/(?P<pk>.+)/$',ModificarCompra.as_view(), name="modificar_compra"),
    url(r'^base', views.base_layout, name='base'),
    url(r'^compras_list', ListadoCompras.as_view(), name="compras_list"),
    url(r'^crear_compra/$', CrearCompra.as_view(), name="crear_compra"),
    path('manifest.json', TemplateView.as_view(template_name='manifest.json', content_type='application/json')),
    path('OneSignalSDKWorker.js', TemplateView.as_view(template_name='OneSignalSDKWorker.js', content_type='application/x-javascript')),
    path('OneSignalSDKWorker.js', TemplateView.as_view(template_name='OneSignalSDKWorker.js', content_type='application/x-javascript')),
    path('onesignal_register/', views.onesignal_register, name='onesignal_register'),
    
]
