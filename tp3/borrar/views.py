from django.http import HttpResponse
from django.template import loader
from foro.models import Topics
def borrar(request):
    template = loader.get_template('borrar/index.html')
    topics = Topics.objects.all().values()
    context = {
    'topics': topics
    }
    return HttpResponse(template.render(context, request))