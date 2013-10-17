from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    choices = (
        ('Urgente','Urgente'),
        ('En Proceso','En Proceso'),
        ('Culminado','Culminado'),
        ('Pausado','Pausado'),
    )
    usuario = models.ForeignKey(User)
    tarea = models.CharField(max_length=100)
    fecha = models.DateField()
    notas = models.TextField(max_length=500)
    hora = models.TimeField()
    cliente = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    estato = models.CharField(max_length=30, choices=choices)
    def __unicode__(self):
        return self.tarea

