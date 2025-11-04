from django.contrib.auth.models import Group, User
from .models import Prodi, Siswa, Kuliah, Registrasi
from rest_framework import serializers

class ProdiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodi
        fields = ['id', 'nama', 'kaprodi']

class SiswaSerializer(serializers.ModelSerializer):
    prodi = serializers.SlugRelatedField(slug_field='nama', queryset=Prodi.objects.all())

    class Meta:
        model = Siswa
        fields = ['id', 'nama', 'nim', 'imagephoto', 'prodi']

class KuliahSerializer(serializers.ModelSerializer):
    prodi = serializers.SlugRelatedField(slug_field='nama', queryset=Prodi.objects.all())

    class Meta:
        model = Kuliah
        fields = ['id', 'matkul', 'prodi', 'hari', 'sks']

class RegistrasiSerializer(serializers.ModelSerializer):
    siswa = serializers.SlugRelatedField(slug_field='nama', queryset=Siswa.objects.all())
    kuliah = serializers.SlugRelatedField(slug_field='matkul', queryset=Kuliah.objects.all())
    class Meta:
        model = Registrasi
        fields = ['id', 'siswa', 'kuliah']