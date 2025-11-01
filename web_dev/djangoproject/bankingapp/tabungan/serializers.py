from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Buku, Transaksi

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_staff"]

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = ["id", "kantor_bank", "nomor_rekening", "nama_nasabah", "alamat"]

class TransaksiSerializer(serializers.ModelSerializer):
    buku = serializers.PrimaryKeyRelatedField(queryset=Buku.objects.all())
    nama_nasabah = serializers.CharField(source='buku.nama_nasabah', read_only=True)

    class Meta:
        model = Transaksi
        fields = ["id", "buku", "nama_nasabah", "tanggal", "jenis", "nominal"]


