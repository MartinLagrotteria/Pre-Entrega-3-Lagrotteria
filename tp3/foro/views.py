from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Topics, Post, Comentario, Usuarios

def foro(request):
  template = loader.get_template('foro/index.html')
  topics = Topics.objects.all().values()
  context = {
    'topics': topics,
    'login' : request.session.get('usuario') and request.session.get('password'),
    'admin' : request.session.get('admin')
  }
  return HttpResponse(template.render(context, request))

def about(request):
  template = loader.get_template('foro/about.html')
  context = {}
  return HttpResponse(template.render(context, request))

def logout(request):
  context = {}
  template = loader.get_template('foro/logout.html')
  if request.session.get('usuario') and request.session.get('password'):
      del request.session['usuario']
      del request.session['password']
      del request.session['admin']
  return HttpResponse(template.render(context, request))

def posteos(request, id_topic):
  topic = Topics.objects.get(id = id_topic)
  posts = Post.objects.filter(topics = topic)
  template = loader.get_template('foro/topic.html')
  usuario = False
  if request.session.get('usuario') and request.session.get('password'):
    usuario = Usuarios.objects.get(usuario = request.session.get('usuario'), password = request.session.get('password'))
  context = {
    'topic' : id_topic,
     "posts" : posts,
     'login' : request.session.get('usuario') and request.session.get('password'),
     'usuario' : usuario,
     'admin' : request.session.get('admin')
  }
  return HttpResponse(template.render(context, request))

def post(request, id_post):
  post = Post.objects.get(id = id_post)
  comentarios = Comentario.objects.filter(post = post)
  usuario = False
  if request.session.get('usuario') and request.session.get('password'):
    usuario = Usuarios.objects.get(usuario = request.session.get('usuario'), password = request.session.get('password'))
  template = loader.get_template('foro/post.html')
  context = {

    'login' : request.session.get('usuario') and request.session.get('password'),
    'admin' : request.session.get('admin'),
    'usuario' : usuario,
    'post' : post,
    'comentarios' : comentarios
  }
  return HttpResponse(template.render(context, request))

