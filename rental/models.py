from django.db import models

class Motor(models.Model):
    merk = models.CharField(max_length=100)
    plat_nomor = models.CharField(max_length=15)
    harga_sewa_per_hari = models.DecimalField(max_digits=10, decimal_places=2)
    tersedia = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.merk} - {self.plat_nomor}"

class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    no_ktp = models.CharField(max_length=20)
    alamat = models.TextField()
    status = models.CharField(max_length=20) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

# class Transaksi(models.Model):
#     motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
#     pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
#     tanggal_sewa = models.DateField()
#     tanggal_kembali = models.DateField()
#     total_harga = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

#     status_pengembalian = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def save(self, *args, **kwargs):
#         selisih_hari = (self.tanggal_kembali - self.tanggal_sewa).days
#         self.total_harga = self.motor.harga_sewa_per_hari * selisih_hari
#         self.motor.tersedia = False
#         self.motor.save()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.pelanggan.nama} - {self.motor.plat_nomor}"
class Transaksi(models.Model):
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    tanggal_sewa = models.DateField()
    tanggal_kembali = models.DateField()
    total_harga = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status_pengembalian = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        selisih_hari = (self.tanggal_kembali - self.tanggal_sewa).days
        self.total_harga = self.motor.harga_sewa_per_hari * selisih_hari
        self.motor.tersedia = False
        self.motor.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pelanggan.nama} - {self.motor.plat_nomor}"