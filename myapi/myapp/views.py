# -*- coding: utf-8 -*-

from rest_framework import generics
from .models import Usuarios, Categorias, Notas, CategoriaNotas, Email
from .serializers import UsuariosSerializer, CategoriasSerializer, NotasSerializer, CategoriaNotasSerializer, EmailSerializer

# Create your views here.
class UsuariosList(generics.ListCreateAPIView):

    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer


class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class CategoriasList(generics.ListCreateAPIView):

    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


class CategoriasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class NotasList(generics.ListCreateAPIView):

    queryset = Notas.objects.all()
    serializer_class = NotasSerializer


class NotasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notas.objects.all()
    serializer_class = NotasSerializer


class CategoriaNotasList(generics.ListCreateAPIView):

    queryset = CategoriaNotas.objects.all()
    serializer_class = CategoriaNotasSerializer


class CategoriaNotasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaNotas.objects.all()
    serializer_class = CategoriaNotasSerializer


class EmailList(generics.ListCreateAPIView):

    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class EmailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
