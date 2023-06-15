from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Topics, Post, Comentario

def foro(request):
  template = loader.get_template('foro/index.html')
  topics = Topics.objects.all().values()
  
  context = {
    'topics': topics,
    'login' : request.session.get('usuario') and request.session.get('password'),
    'admin' : request.session.get('admin')
  }
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
  posts = Post.objects.filter(topics = id_topic).values()
  template = loader.get_template('foro/topic.html')
  context = {
    'topic' : id_topic,
     "posts" : posts,
     'login' : request.session.get('usuario') and request.session.get('password'),
     'admin' : request.session.get('admin')
  }
  return HttpResponse(template.render(context, request))

def post(request, id_post):
  post = Post.objects.get(id = id_post)
  comentarios = Comentario.objects.filter(post = post).values()
  template = loader.get_template('foro/post.html')
  context = {
    'login' : request.session.get('usuario') and request.session.get('password'),
    'admin' : request.session.get('admin'),
    'post' : post,
    'comentarios' : comentarios
  }
  return HttpResponse(template.render(context, request))

