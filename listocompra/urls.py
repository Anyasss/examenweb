"""listocompra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from blog.quickstart import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import path

router = routers.DefaultRouter()

router.register(r'Tiendas', views.TiendaViewSet)
router.register(r'Ciudad', views.CiudadViewSet)
router.register(r'Region', views.RegionViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^password/', include('password_reset.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),   
    url(r'^', include(router.urls)),
    path('', include('pwa.urls')),
]

