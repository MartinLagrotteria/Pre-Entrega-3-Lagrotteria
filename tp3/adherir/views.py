from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from foro.models import Topics


def adherir(request):
    template = loader.get_template('adherir/index.html')
    
    topics = Topics.objects.all().values()
    context = {
    'topics': topics
    }

    return HttpResponse(template.render(context, request))