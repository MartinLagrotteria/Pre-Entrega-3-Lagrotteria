from django.urls import path
from . import views
from django.urls import include
app_name = 'foro'

urlpatterns = [
    path('', views.foro, name='foro'),
    path('logout/', views.logout, name='logout'),
    path('topic/<int:id_topic>/', views.posteos, name='posteos'),
    path('post/<int:id_post>/', views.post, name='posteo')
]