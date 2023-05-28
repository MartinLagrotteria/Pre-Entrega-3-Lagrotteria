from django.db import models

class Topics(models.Model):
  nombre = models.CharField(max_length=255)
  