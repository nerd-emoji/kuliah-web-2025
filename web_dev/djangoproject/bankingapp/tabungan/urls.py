from django.urls import path
from . import views

app_name = "tabungan"
urlpatterns = [
    path("",views.list_buku, name="list-buku"),
    path("buku/create", views.create_buku, name="create_buku"),
    path("buku/update/<int:buku_id>/", views.update_buku, name="update-buku"),
    path("buku/delete/<int:buku_id>/", views.delete_buku, name="delete-buku"),
    path('buku/detail_transaksi/<int:buku_id>/', views.detail_transaksi, name='detail-transaksi'),
    path('buku/create_transaksi/<int:buku_id>/', views.create_transaksi, name='create-transaksi'),
]