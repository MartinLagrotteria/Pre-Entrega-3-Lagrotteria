from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from foro.models import Usuarios
from django.template import loader
from django.shortcuts import redirect
def comprobarUsuario(usuario:str,password:str) -> bool:
  return Usuarios.objects.filter(usuario=usuario,password=password).exists()
def getAdmin(usuario:str) -> bool:
  return Usuarios.objects.get(usuario=usuario).admin

def login(request):
  context = {}
  template = loader.get_template('login/login.html')
  template_exito = loader.get_template('foro/index.html')
  template_error = loader.get_template('login/login_error.html')
  
  if request.method == 'POST':
    usuario = request.POST['usuario']
    password = request.POST['password']
    if comprobarUsuario(usuario,password):
      request.session['usuario'] = usuario
      request.session['password'] = password
      request.session['admin'] = getAdmin(usuario)
      return HttpResponseRedirect('/index/')
    else:
      return HttpResponse(template_error.render(context, request))
  return HttpResponse(template.render(context, request))
