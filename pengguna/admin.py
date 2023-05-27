from django.contrib import admin
# ada titiknya agar bisa ambil models barang dll yg namanya model
from .models import ProdukItem
from .models import Pembeli

class ProdukItemAdmin(admin.ModelAdmin):
    list_display = ('nama_produk', 'harga', 'harga_diskon', 'slug', 'deskripsi', 'gambar', 'label', 'kategori')
# Register your models here.

class PembeliAdmin(admin.ModelAdmin):
    list_display= ('nama', 'email', 'alamat', 'no_hp')

admin.site.register(ProdukItem, ProdukItemAdmin)
admin.site.register(Pembeli, PembeliAdmin)
