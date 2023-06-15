from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from foro.models import Topics

def checkearNombre(nombre:str) -> bool:
    if nombre is None or len(nombre) == 0:
        return False
    return True

def adherir(request):
    template = loader.get_template('adherir/index.html')
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