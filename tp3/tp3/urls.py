from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', include('foro.urls', namespace='foro')),
    path('adherir/', include('adherir.urls', namespace='adherir')),
    path('borrar/', include('borrar.urls', namespace='borrar')),
    #path('index/', include('foro.urls', namespace='foro')),
    path('login/', include('login.urls', namespace='login')),
    path('registro/', include('registro.urls', namespace='registro')),
    path('index/logout/', include('foro.urls', namespace='logout')),
    path('index/', include('foro.urls', namespace='posteos')),
    path('index/', include('foro.urls', namespace='posteo')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
