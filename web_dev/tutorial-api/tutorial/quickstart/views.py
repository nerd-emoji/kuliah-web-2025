from django.shortcuts import render
from django.contrib.auth.models import Group, User
from .models import Prodi, Siswa, Kuliah, Registrasi
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer, ProdiSerializer, SiswaSerializer, KuliahSerializer, RegistrasiSerializer


class UserViewSet(viewsets.ModelViewSet):


    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProdiViewSet(viewsets.ModelViewSet):
    queryset = Prodi.objects.all()
    serializer_class = ProdiSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'nama', 'kaprodi']
    search_fields = ['nama', 'kaprodi']
    ordering_fields = ['nama', 'kaprodi']

class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['prodi', 'nim', 'id']
    search_fields = ['nama', 'nim']
    ordering_fields = ['nama', 'nim']

class KuliahViewSet(viewsets.ModelViewSet):
    queryset = Kuliah.objects.all()
    serializer_class = KuliahSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['prodi', 'hari', 'sks', 'id']
    search_fields = ['matkul', 'hari']
    ordering_fields = ['matkul', 'sks']

class RegistrasiViewSet(viewsets.ModelViewSet):
    queryset = Registrasi.objects.all()
    serializer_class = RegistrasiSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['siswa', 'kuliah', 'id']
    search_fields = []
    ordering_fields = ['id']
