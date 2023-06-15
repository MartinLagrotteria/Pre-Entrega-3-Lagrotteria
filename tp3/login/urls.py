from django.urls import path,re_path
from . import views
from django.views.generic import RedirectView
app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    re_path("index/", RedirectView.as_view(url='/index/')),
]