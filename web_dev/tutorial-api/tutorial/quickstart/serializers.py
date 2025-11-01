from django.contrib.auth.models import Group, User
from .models import Prodi, Siswa, Kuliah, Registrasi
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
        
class ProdiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodi
        fields = ['id', 'nama', 'kaprodi']

class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = ['id', 'nama', 'nim', 'imagephoto', 'prodi']

class KuliahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kuliah
        fields = ['id', 'matkul', 'hari', 'sks', 'prodi']

class RegistrasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrasi
        fields = ['id', 'siswa', 'kuliah']