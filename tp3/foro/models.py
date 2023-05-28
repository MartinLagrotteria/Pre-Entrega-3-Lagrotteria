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
  titulo = models.CharField(max_length=255)
  contenido = models.TextField()
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  def __str__(self):
      return self.titulo