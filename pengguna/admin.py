from django.contrib import admin
# ada titiknya agar bisa ambil models barang dll yg namanya model
from .models import ProdukItem

class ProdukItemAdmin(admin.ModelAdmin):
    list_display = ('nama_produk', 'harga', 'harga_diskon', 'slug', 'deskripsi', 'gambar', 'label', 'kategori')
# Register your models here.

admin.site.register(ProdukItem, ProdukItemAdmin)
