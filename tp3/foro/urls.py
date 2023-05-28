from django.urls import path
from . import views
from django.urls import include
app_name = 'foro'

urlpatterns = [
    path('foro/', views.foro, name='foro'),

]