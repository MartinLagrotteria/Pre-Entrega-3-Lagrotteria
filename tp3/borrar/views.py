from django.http import HttpResponse
from django.template import loader
from foro.models import Topics
def borrar(request):
    template = loader.get_template('borrar/index.html')
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