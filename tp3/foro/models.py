from django.db import models

class Topics(models.Model):
  nombre = models.CharField(max_length=255)
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  def __str__(self):
      return self.nombre

class Usuarios(models.Model):
  usuario = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  perfil_imagen = models.ImageField(null=True, blank=True, upload_to = 'avatares/', default = 'avatares/borrar.png')
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  admin = models.BooleanField(default=False) 
  def __str__(self):
      return self.usuario
  

class Post(models.Model):
  usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
  topics = models.ForeignKey(Topics, on_delete=models.CASCADE)
  titulo = models.CharField(max_length=255)
  contenido = models.TextField()
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  def __str__(self):
      return self.titulo
  
class Comentario(models.Model):
  usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  contenido = models.TextField()
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  def __str__(self):
      return self.contenido
