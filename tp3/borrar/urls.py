from django.urls import path,re_path
from . import views
from django.views.generic import RedirectView

app_name = 'borrar'
urlpatterns = [
    path('topic/', views.borrar_topic, name='topic'),
    path('comentario/<int:id_comentario>/', views.borrar_comentario, name='comentario'),
    path('post/<int:id_post>/', views.borrar_post, name='post'),
    re_path("post/<int:id_post>/", RedirectView.as_view(url='/post/')),
     re_path("topic/<int:id_topic>/", RedirectView.as_view(url='/topic/')),
]