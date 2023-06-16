from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from foro.models import Topics,Post,Usuarios,Comentario

def checkearNombre(nombre:str) -> bool:
    if nombre is None or len(nombre) == 0:
        return False
    return True

def checkearContenido(contenido:str) -> bool:
    if contenido is None or len(contenido) == 0: #No hay contenido
        return False
    elif len(contenido) < 10: #Contenido muy corto
        return False
    elif len(contenido) > 500: #Contenido muy largo
        return False
    elif '<' in contenido or '>' in contenido: #Contenido mal formado
        return False
    return True

def checkearTitulo(contenido:str) -> bool:
    if contenido is None or len(contenido) == 0: #No hay contenido
        return False
    elif len(contenido) < 3: #Contenido muy corto
        return False
    elif len(contenido) > 50: #Contenido muy largo
        return False
    elif '<' in contenido or '>' in contenido: #Contenido mal formado
        return False
    return True

def adherir_topic(request):
    if not(request.session.get('admin')):
        return HttpResponseRedirect('/index/')
    template = loader.get_template('adherir/topic.html')
    template_exito = loader.get_template('adherir/exito.html')
    template_error = loader.get_template('adherir/error.html')
    topics = Topics.objects.all().values()
    context = {
    'topics': topics
    }
    if request.method == 'POST':
        nombre = request.POST['nombre']
        if checkearNombre(nombre):
            Topics(nombre=nombre).save()
            return HttpResponse(template_exito.render(context, request))
        else:
            return HttpResponse(template_error.render(context, request))
    return HttpResponse(template.render(context, request))

def adherir_post(request, id_topic):
    usuario = request.session.get('usuario')
    password = request.session.get('password')
    if not(usuario and password):
        return HttpResponseRedirect('/index/')
    context= {
        'topic': Topics.objects.get(id=id_topic)
    }
    if request.method == 'POST':
        titulo = request.POST['titulo']
        contenido = request.POST['contenido']
        if checkearContenido(contenido) and checkearTitulo(titulo):
            Post(usuario = Usuarios.objects.get(usuario = usuario, password = password) ,topics = Topics.objects.get(id=id_topic),titulo=titulo, contenido=contenido).save()
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponseRedirect('/index/')
    template = loader.get_template('adherir/post.html')
    return HttpResponse(template.render(context, request))

def adherir_comentario(request, id_post):
    usuario = request.session.get('usuario')
    password = request.session.get('password')
    if not(usuario and password):
        return HttpResponseRedirect('/index/')
    if request.method == 'POST':
        contenido = request.POST['contenido']
        if checkearContenido(contenido):
            Comentario(usuario = Usuarios.objects.get(usuario = usuario, password = password) ,post = Post.objects.get(id=id_post), contenido=contenido).save()
            return HttpResponseRedirect('/post/'+str(id_post))
    return HttpResponseRedirect('/index/')

def adherir_avatar(request):
    usuario = request.session.get('usuario')
    password = request.session.get('password')
    if not(usuario and password):
        return HttpResponseRedirect('/index/')
    usuario = Usuarios.objects.get(usuario = usuario, password = password)
    context = {
        'usuario' : usuario
    }
    template = loader.get_template('adherir/cargarAvatar.html')
    if request.method == 'POST':
        avatar = request.FILES['avatar']
        usuario.perfil_imagen = avatar
        usuario.save()
       
        return HttpResponseRedirect('/index/')
    return HttpResponse(template.render(context, request))