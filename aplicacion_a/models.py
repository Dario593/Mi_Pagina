from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField, FileField


class Musica(models.Model):
    nombre = CharField(max_length=200)
    titulo = CharField(max_length=100)
    portada = ImageField(upload_to="aplicacion_a/images/")
    audio = FileField(upload_to="aplicacion_a/audios/")


class Principal(models.Model):
    titulo = CharField(max_length=200)
    portada = ImageField(upload_to="aplicacion_a/portada")
    parrafo = TextField(max_length=600)
    url = CharField(max_length=100, blank=True)
