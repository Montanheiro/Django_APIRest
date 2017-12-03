# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuarios(models.Model):
    
    class Meta:
        db_table='usuarios'
    
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

class Categorias(models.Model):
    
    class Meta:
        db_table='categorias'
        
    nome = models.CharField(max_length=255)

class Notas(models.Model):
    
    class Meta:
        db_table='notas'
    
    usuario = models.ForeignKey('Usuarios', related_name='notas')
    titulo = models.CharField(max_length=255)
    nota = models.CharField(max_length=200)

class CategoriaNotas(models.Model):
    
    class Meta:
        db_table='categoriasnotas'
    
    categorias_id = models.ForeignKey('Categorias', related_name='categoriasnotas')
    notas_id = models.ForeignKey(Notas, on_delete=models.CASCADE)

class Email(models.Model):
    
    class Meta:
        db_table='email'
    
    enderecoEmail = models.CharField(max_length=255)
    usuarios_id = models.ForeignKey('Usuarios', related_name='email')

