"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'prodi', views.ProdiViewSet)
router.register(r'siswa', views.SiswaViewSet)
router.register(r'kuliah', views.KuliahViewSet)
router.register(r'registrasi', views.RegistrasiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/siswa/prodi/<str:prodi_nama>/', views.SiswaByProdiList.as_view()),
    path('api/siswa/kaprodi/<str:kaprodi_nama>/', views.SiswaByKaprodiList.as_view()),
    path('api/registrasi/siswa/<str:siswa_nama>/', views.RegistrasiBySiswaList.as_view()),
    path('api/registrasi/kuliah/<str:kuliah_matkul>/', views.RegistrasiByKuliahList.as_view()),
    path('api/registrasi/kaprodi/<str:kaprodi_nama>/', views.RegistrasiByKaprodiList.as_view()),
    path('api/kuliah/kaprodi/<str:kaprodi_nama>/', views.KuliahByKaprodiList.as_view()),
    path('api/kuliah/prodi/<str:prodi_nama>/', views.KuliahByProdiList.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
