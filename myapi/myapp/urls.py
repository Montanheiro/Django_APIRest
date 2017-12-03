from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^usuarios/$', views.UsuariosList.as_view(), name='usuarios-list'),
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.UsuariosDetail.as_view(), name='usuarios-detail'),

    url(r'^categorias/$', views.CategoriasList.as_view(), name='categorias-list'),
    url(r'^categoria/(?P<pk>[0-9]+)/$', views.CategoriasDetail.as_view(), name='categorias-detail'),

    url(r'^notas/$', views.NotasList.as_view(), name='notas-list'),
    url(r'^nota/(?P<pk>[0-9]+)/$', views.NotasDetail.as_view(), name='notas-detail'),

    url(r'^categoriasnotas/$', views.CategoriaNotasList.as_view(), name='categoriasnotas-list'),
    url(r'^categoriasnota/(?P<pk>[0-9]+)/$', views.CategoriaNotasDetail.as_view(), name='categoriasnotas-detail'),

    url(r'^emails/$', views.EmailList.as_view(), name='emails-list'),
    url(r'^email/(?P<pk>[0-9]+)/$', views.EmailDetail.as_view(), name='emails-detail'),
]
