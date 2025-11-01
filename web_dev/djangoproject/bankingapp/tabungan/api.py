from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers, permissions

from .models import Buku, Transaksi
from .serializers import UserSerializer, GroupSerializer, BukuSerializer, TransaksiSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all().order_by('id')
    serializer_class = BukuSerializer
    permission_classes = [permissions.IsAuthenticated] 
    pagination_class = None

class TransaksiViewSet(viewsets.ModelViewSet):
    queryset = Transaksi.objects.all().order_by('-tanggal')
    serializer_class = TransaksiSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'buku', BukuViewSet, basename='buku')
router.register(r'transaksi', TransaksiViewSet, basename='transaksi')