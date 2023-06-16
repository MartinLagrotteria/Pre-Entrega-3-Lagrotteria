from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from foro.models import Topics,Comentario,Usuarios,Post

def checkearCreadorComentario(usuario:str, password:str, id_comentario: int):
    return Usuarios.objects.get(usuario=usuario, password = password) == Comentario.objects.get(id=id_comentario).usuario
def checkearCreadorPost(usuario:str, password:str, id_post: int):
    return Usuarios.objects.get(usuario=usuario, password = password) == Post.objects.get(id=id_post).usuario

def borrar_topic(request):
    template = loader.get_template('borrar/topic.html')
    template_exito = loader.get_template('borrar/exito.html')
    topics = Topics.objects.all().values()
    context = {
    'topics': topics
    }
    if request.method == 'POST':
        id = request.POST["id"]
        Topics.objects.filter(id=id).delete()
        
        return HttpResponse(template_exito.render(context, request))
    return HttpResponse(template.render(context, request))
def borrar_comentario(request, id_comentario):
    id_post = Comentario.objects.get(id=comentario_id).post.id # type: ignore
    usuario = request.session['usuario']
    password = request.session['password']
    admin = request.session['admin']
    if admin or checkearCreadorComentario(usuario, password, id_comentario):
        Comentario.objects.get(id=id_comentario).delete()
    return HttpResponseRedirect('/post/'+str(id_post))

def borrar_post(request, id_post):
    id_topic = Post.objects.get(id=id_post).topics.id # type: ignore
    usuario = request.session['usuario']
    password = request.session['password']
    admin = request.session['admin']
    if admin or checkearCreadorPost(usuario, password, id_post):
        Post.objects.get(id=id_post).delete()
    return HttpResponseRedirect('/topic/'+str(id_topic))
