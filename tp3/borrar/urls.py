from django.urls import path
from . import views
app_name = 'borrar'
urlpatterns = [
    path('borrar/', views.borrar, name='borrar'),
]