
from rest_framework import serializers
from .models import Usuarios, Categorias, Notas, CategoriaNotas, Email

class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Usuarios
        fields = '__all__'

class CategoriasSerializer(serializers.ModelSerializer):

    class Meta:

        model = Categorias
        fields = '__all__'

class NotasSerializer(serializers.ModelSerializer):

    class Meta:

        model = Notas
        fields = '__all__'

class CategoriaNotasSerializer(serializers.ModelSerializer):

    class Meta:

        model = CategoriaNotas
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):

    class Meta:

        model = Email
        fields = '__all__'        
