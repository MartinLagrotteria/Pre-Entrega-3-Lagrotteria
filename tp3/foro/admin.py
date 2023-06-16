from django.contrib import admin
from foro.models import *
# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Topics)
admin.site.register(Post)
admin.site.register(Comentario)