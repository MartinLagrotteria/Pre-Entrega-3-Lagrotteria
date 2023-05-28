from django.urls import path
from . import views
app_name = 'adherir'
urlpatterns = [
    path('adherir/', views.adherir, name='adherir'),
]