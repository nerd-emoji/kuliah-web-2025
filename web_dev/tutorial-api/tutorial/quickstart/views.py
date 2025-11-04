from django.shortcuts import render
from .models import Prodi, Siswa, Kuliah, Registrasi
from rest_framework import permissions, viewsets, filters, generics
# from django_filters.rest_framework import DjangoFilterBackend

from tutorial.quickstart.serializers import ProdiSerializer, SiswaSerializer, KuliahSerializer, RegistrasiSerializer
    
class ProdiViewSet(viewsets.ModelViewSet):
    queryset = Prodi.objects.all()
    serializer_class = ProdiSerializer
    permission_classes = [permissions.AllowAny]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['id', 'nama', 'kaprodi']
    # search_fields = ['nama', 'kaprodi']
    # ordering_fields = ['nama', 'kaprodi']

class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer
    permission_classes = [permissions.AllowAny]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['prodi', 'nim', 'id']
    # search_fields = ['nama', 'nim']
    # ordering_fields = ['nama', 'nim']

class KuliahViewSet(viewsets.ModelViewSet):
    queryset = Kuliah.objects.all()
    serializer_class = KuliahSerializer
    permission_classes = [permissions.AllowAny]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['prodi', 'hari', 'sks', 'id']
    # search_fields = ['matkul', 'hari']
    # ordering_fields = ['matkul', 'sks']

class RegistrasiViewSet(viewsets.ModelViewSet):
    queryset = Registrasi.objects.all()
    serializer_class = RegistrasiSerializer
    permission_classes = [permissions.AllowAny]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['siswa', 'kuliah', 'id']
    # search_fields = []
    # ordering_fields = ['id']

class SiswaByProdiList(generics.ListAPIView):
    serializer_class = SiswaSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        prodi_nama = self.kwargs.get('prodi_nama')
        if not prodi_nama:
            return Siswa.objects.none()
        return Siswa.objects.filter(prodi__nama__iexact=prodi_nama)

class KuliahByProdiList(generics.ListAPIView):
    serializer_class = KuliahSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        prodi_nama = self.kwargs.get('prodi_nama')
        if not prodi_nama:
            return Kuliah.objects.none()
        return Kuliah.objects.filter(prodi__nama__iexact=prodi_nama)

class RegistrasiBySiswaList(generics.ListAPIView):
    serializer_class = RegistrasiSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        siswa_nama = self.kwargs.get('siswa_nama')
        if not siswa_nama:
            return Registrasi.objects.none()
        return Registrasi.objects.filter(siswa__nama__iexact=siswa_nama)

class RegistrasiByKuliahList(generics.ListAPIView):
    serializer_class = RegistrasiSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        kuliah_matkul = self.kwargs.get('kuliah_matkul')
        if not kuliah_matkul:
            return Registrasi.objects.none()
        return Registrasi.objects.filter(kuliah__matkul__iexact=kuliah_matkul)

class SiswaByKaprodiList(generics.ListAPIView):
    serializer_class = SiswaSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        kaprodi_nama = self.kwargs.get('kaprodi_nama')
        if not kaprodi_nama:
            return Siswa.objects.none()
        return Siswa.objects.filter(prodi__kaprodi__iexact=kaprodi_nama)


class KuliahByKaprodiList(generics.ListAPIView):
    serializer_class = KuliahSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        kaprodi_nama = self.kwargs.get('kaprodi_nama')
        if not kaprodi_nama:
            return Kuliah.objects.none()
        return Kuliah.objects.filter(prodi__kaprodi__iexact=kaprodi_nama)


class RegistrasiByKaprodiList(generics.ListAPIView):
    serializer_class = RegistrasiSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        kaprodi_nama = self.kwargs.get('kaprodi_nama')
        if not kaprodi_nama:
            return Registrasi.objects.none()
        # semua registrasi untuk kuliah yang berasal dari Prodi dengan kaprodi tertentu
        return Registrasi.objects.filter(kuliah__prodi__kaprodi__iexact=kaprodi_nama)
    