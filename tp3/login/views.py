from django.shortcuts import render
from django.http import HttpResponse
from foro.models import Usuarios
from django.template import loader
  
def comprobarUsuario(usuario:str,password:str, usuarios:Usuarios) -> bool:
  return usuarios.filter(usuario=usuario,password=password).exists()

def login(request):
  context = {}
  template = loader.get_template('login/login.html')
  template_exito = loader.get_template('foro/index.html')
  template_error = loader.get_template('login/login_error.html')
  
  if request.method == 'POST':
    usuarios = Usuarios.objects
    usuario = request.POST['usuario']
    password = request.POST['password']
    if comprobarUsuario(usuario,password,usuarios):
      request.session['usuario'] = usuario
      request.session['password'] = password
      return HttpResponse(template_exito.render(context, request))
    else:
      return HttpResponse(template_error.render(context, request))
  return HttpResponse(template.render(context, request))
