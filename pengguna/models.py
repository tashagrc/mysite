from django.db import models

# Create your models here.
#label
PILIHAN_LABEL = (
    ("BS", "best seller"),
    ("BQ", "best quality"),
)

PILIHAN_KATEGORI = (
    ("1", "Computer"),
    ("2", "Accesories"),
)
# null = True itu artinya opsional
class ProdukItem(models.Model):
    nama_produk = models.CharField(max_length=255)
    harga = models.FloatField()
    harga_diskon = models.FloatField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='product_picts', null=True)
    label = models.CharField(choices=PILIHAN_LABEL, max_length=4)
    kategori = models.CharField(choices=PILIHAN_KATEGORI, max_length=2)

    def __str__(self):
        return f"{self.nama_produk} - ${self.harga}"
    
class Pembeli(models.Model):
# nama, email, alamat, no hp
    nama = models.CharField(max_length=255)
    email = models.EmailField()
    alamat = models.TextField()
    no_hp = models.CharField(max_length=255)