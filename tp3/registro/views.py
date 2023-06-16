from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from foro.models import Usuarios



def comprobarPass(password:str) -> bool:
  if password == '':
    return False
  elif len(password) < 8:
    return False
  elif not password.isalnum():
    return False
  elif not password.islower():
    return False
  else:
    return True
  

def comprobarUser(usuario:str, usuarios) -> bool:
  if usuario == "":
    return False
  elif usuario in usuarios.values_list('usuario'):
    return False
  elif len(usuario) < 5:
    return False
  else:
    return True

def comprobarEmail(email:str, usuarios) -> bool:
  if email == "":
    return False
  elif not("@" in email) and not(".com" in email):
    return False
  elif email in usuarios.values_list('email'):
    return False
  else:
    return True
  

def registro(request):
  context = {}
  template = loader.get_template('registro/registro.html')
  template_exito = loader.get_template('registro/registro_exito.html')
  template_error = loader.get_template('registro/registro_error.html')
  
  if request.method == 'POST':
    usuarios = Usuarios.objects.all() #lista de nombres de usuarios
    usuario = request.POST['usuario']
    password = request.POST['password']
    email = request.POST['email']
    avatar = request.FILES['avatar']
    if comprobarEmail(email,usuarios) and comprobarPass(password) and comprobarUser(usuario,usuarios):
      Usuarios(usuario=usuario,email=email,password=password, perfil_imagen = avatar).save()
      return HttpResponse(template_exito.render(context, request))
    else:
      return HttpResponse(template_error.render(context, request))
  
  return HttpResponse(template.render(context, request))

'''
def adherir(request):
    template = loader.get_template('adherir/index.html')
    template_exito = loader.get_template('adherir/exito.html')
    topics = Topics.objects.all().values()
    context = {
    'topics': topics
    }

    if request.method == 'POST':
        nombre = request.POST['nombre']
        Topics(nombre=nombre).save()
        
        return HttpResponse(template_exito.render(context, request))
    return HttpResponse(template.render(context, request))
'''
 