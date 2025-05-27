# rental/forms.py
from django import forms
from .models import Motor, Pelanggan, Transaksi

class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = '__all__'

class PelangganForm(forms.ModelForm):
    class Meta:
        model = Pelanggan
        fields = '__all__'

# class TransaksiForm(forms.ModelForm):
#     class Meta:
#         model = Transaksi
#         fields = '__all__'
#         widgets = {
#             'tanggal_sewa': forms.DateInput(attrs={'type': 'date'}),
#             'tanggal_kembali': forms.DateInput(attrs={'type': 'date'}),
#         }


class TransaksiForm(forms.ModelForm):
    class Meta:
        model = Transaksi
        fields = '__all__'
        widgets = {
            'tanggal_sewa': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tanggal_kembali': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
