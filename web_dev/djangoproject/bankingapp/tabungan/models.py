from django.db import models

# Create your models here.

#BUKU
# Kantor bank
# Nomor Rekening
# Nama
# Alamat

class Buku(models.Model):
    kantor_bank = models.CharField(max_length=200)
    nomor_rekening = models.CharField(max_length=20, unique=True)
    nama_nasabah = models.CharField(max_length=200)
    alamat = models.TextField(max_length=200)
    
    def __str__(self):
        return self.nama_nasabah

class Transaksi(models.Model):
    JENIS_TRANSAKSI = [
        ('debit', 'Debit'),
        ('kredit', 'Kredit'),
    ]
    
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    tanggal = models.DateTimeField(auto_now_add=True)
    nominal = models.DecimalField(max_digits=15, decimal_places=2)
    jenis = models.CharField(max_length=10, choices=JENIS_TRANSAKSI)

    def __str__(self):
        return f"{self.buku.nama_nasabah} - {self.tanggal} - {self.nominal}"

