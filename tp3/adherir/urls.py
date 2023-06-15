from django.urls import path,re_path
from . import views
from django.views.generic import RedirectView
app_name = 'adherir'
urlpatterns = [
    path('topic/', views.adherir_topic, name='topic'),
    path('post/<int:id_topic>/', views.adherir_post, name='post'),
    path('comentario/<int:id_post>/', views.adherir_comentario, name='comentario'),
    re_path("index/", RedirectView.as_view(url='/index/')),
    re_path("post/<int:id_post>/", RedirectView.as_view(url='/post/')),
]