from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from foro.models import Topics


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