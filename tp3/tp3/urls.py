"""
URL configuration for tp3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""from django.contrib import admin
from django.urls import path, include
from django.urls import path
from foro import views as foroviews
from adherir import views as adherirviews  
from borrar import views as borrarviews

urlpatterns = [
    path('foro/', foroviews.foro, name='foro'),
    path('adherir/', adherirviews.adherir, name='adherir'),
    path('borrar/', borrarviews.borrar, name='borrar'),
    path('adherir/', include('adherir.urls', namespace='adherir')),
    path('borrar/', include('borrar.urls', namespace='borrar'))
]"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('', include('foro.urls')),
    #path('', include('adherir.urls')),
    #path('', include('borrar.urls')),
    path('admin/', admin.site.urls),
    path('adherir/', include('adherir.urls', namespace='adherir')),
    path('borrar/', include('borrar.urls', namespace='borrar')),
    path('foro/', include('foro.urls', namespace='foro'))
]
