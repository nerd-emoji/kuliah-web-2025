from django.db import models

# Create your models here.
class Prodi(models.Model):
    nama = models.CharField(max_length=100)
    kaprodi = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nama
    
class Siswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20, unique=True)
    imagephoto = models.ImageField(upload_to='photos/')
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

class Kuliah(models.Model):
    matkul = models.CharField(max_length=100)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    hari = models.CharField(max_length=20)
    sks = models.IntegerField()

    def __str__(self):
        return self.matkul

class Registrasi(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    kuliah = models.ForeignKey(Kuliah, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.siswa.nama} - {self.kuliah.matkul}"