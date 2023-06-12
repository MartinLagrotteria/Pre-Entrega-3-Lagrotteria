from django.db import models
from datetime import datetime
class Topics(models.Model):
  nombre = models.CharField(max_length=255)
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  def __str__(self):
      return self.nombre

class Usuario(models.Model):
  nombre = models.CharField(max_length=255)
  apellido = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  def __str__(self):
      return self.nombre
  

class Post(models.Model):
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  topics = models.ForeignKey(Topics, on_delete=models.CASCADE)
  titulo = models.CharField(max_length=255)
  contenido = models.TextField()
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  def __str__(self):
      return self.titulo
  
class Comentario(models.Model):
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  contenido = models.TextField()
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  def __str__(self):
      return self.contenido
  
class Login(Usuario):
   
   def check_password(self, password):
       if password == self.password:
           return True
       return False 
   
   def check_username(self, nombre):
       if self.nombre == nombre:
           return True
       return False

