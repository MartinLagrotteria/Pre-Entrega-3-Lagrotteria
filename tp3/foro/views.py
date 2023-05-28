
from django.http import HttpResponse
from django.template import loader
from .models import Topics
def foro(request):
  template = loader.get_template('foro/index.html')
  topics = Topics.objects.all().values()
  context = {
    'topics': topics
  }
  return HttpResponse(template.render(context, request))