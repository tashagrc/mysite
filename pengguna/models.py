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

class ProdukItem(models.Model):
    nama_produk = models.CharField(max_length=255)
    harga = models.FloatField()
    harga_diskon = models.FloatField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='product_picts')
    label = models.CharField(choices=PILIHAN_LABEL, max_length=4)
    kategori = models.CharField(choices=PILIHAN_KATEGORI, max_length=2)

    def __str__(self):
        return f"{self.nama_produk} - ${self.harga}"