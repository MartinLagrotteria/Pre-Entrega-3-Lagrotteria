from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    path('', include('foro.urls')),
    path('adherir/', include('adherir.urls', namespace='adherir')),
    path('borrar/', include('borrar.urls', namespace='borrar')),
    path('index/', include('foro.urls', namespace='foro')),
    path('login/', include('login.urls', namespace='login')),
    path('registro/', include('registro.urls', namespace='registro')),
    path('index/logout/', include('foro.urls', namespace='logout')),
    path('index/', include('foro.urls', namespace='posteos')),
    path('index/', include('foro.urls', namespace='posteo'))
]
