# rental/forms.py
from django import forms
from .models import Motor, Pelanggan, Transaksi

class MotorForm(forms.ModelForm):
    STATUS_TERSEDIA = [
        (True, '✅ Tersedia'),
        (False, '❌ Tidak Tersedia'),
    ]

    tersedia = forms.ChoiceField(
        choices=STATUS_TERSEDIA,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Motor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MotorForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Jangan override class di field 'tersedia' karena sudah pakai 'form-select'
            if field_name != 'tersedia':
                field.widget.attrs.update({'class': 'form-control'})

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
