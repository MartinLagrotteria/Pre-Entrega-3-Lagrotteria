from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Topics, Post, Usuarios

def foro(request):
  template = loader.get_template('foro/index.html')
  topics = Topics.objects.all().values()
  
  context = {
    'topics': topics,
    'login' : not(request.session.get('usuario') and request.session.get('password'))
  }
  return HttpResponse(template.render(context, request))

def posteos(request, id_topic):
  posts = Post.objects.filter(topics = id_topic).values()
  template = loader.get_template('foro/post.html')
  context = {
     "posts" : posts,
     'login' : not(request.session.get('usuario') and request.session.get('password'))
  }
  return HttpResponse(template.render(context, request))

def logout(request):
  context = {}
  template = loader.get_template('foro/logout.html')
  if request.session.get('usuario') and request.session.get('password'):
      del request.session['usuario']
      del request.session['password']
  return HttpResponse(template.render(context, request))
