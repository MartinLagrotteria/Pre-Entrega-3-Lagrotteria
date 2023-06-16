from django.urls import path,re_path
from . import views
from django.views.generic import RedirectView
app_name = 'foro'

urlpatterns = [
    path('', views.foro, name='foro'),
    path('logout/', views.logout, name='logout'),
    path('topic/<int:id_topic>/', views.posteos, name='posteos'),
    path('post/<int:id_post>/', views.post, name='posteo'),
    path('about/', views.about, name='about'),
    path('perfil/', views.perfil, name='pefil'),
    re_path("/volver", RedirectView.as_view(url='/index/')),
]