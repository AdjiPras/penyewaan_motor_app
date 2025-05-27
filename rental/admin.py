# rental/admin.py
from django.contrib import admin
from .models import Motor, Pelanggan, Transaksi

admin.site.register(Motor)
admin.site.register(Pelanggan)
admin.site.register(Transaksi)