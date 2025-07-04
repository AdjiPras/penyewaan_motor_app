# rental/forms.py
from django import forms
from .models import Motor, Pelanggan, Transaksi

class MotorForm(forms.ModelForm):
    STATUS_CHOICES = (
        (True, '✅ Tersedia'),
        (False, '❌ Tidak Tersedia'),
    )
    tersedia = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = Motor
        fields = ['merk', 'plat_nomor', 'harga_sewa_per_hari', 'tersedia', 'jumlah_unit']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tambahkan class bootstrap form-control untuk semua field kecuali tersedia (karena sudah form-select)
        for field_name, field in self.fields.items():
            if field_name != 'tersedia':
                field.widget.attrs.update({'class': 'form-control'})

class PelangganForm(forms.ModelForm):
    class Meta:
        model = Pelanggan
        fields = ['nama', 'jenis_kelamin', 'no_ktp', 'status', 'alamat']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class TransaksiForm(forms.ModelForm):
    total_harga = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'form-control'
        })
    )
    class Meta:
        model = Transaksi
        fields = [
            'motor',
            'pelanggan',
            'tanggal_sewa',
            'tanggal_kembali',
            'status_pengembalian'
        ]
        widgets = {
            'tanggal_sewa': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'tanggal_kembali': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'status_pengembalian': forms.Select(
                choices=[(True, 'Sudah'), (False, 'Belum')],
                attrs={'class': 'form-control'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tambahkan label kosong custom untuk dropdown FK
        self.fields['motor'].empty_label = "Pilih Motor: "
        self.fields['pelanggan'].empty_label = "Pilih Pelanggan: "

        # Tambahkan class form-control ke semua field (kecuali status_pengembalian yang sudah)
        for name, field in self.fields.items():
            if name not in ['status_pengembalian', 'tanggal_sewa', 'tanggal_kembali']:
                field.widget.attrs.update({'class': 'form-control'})


