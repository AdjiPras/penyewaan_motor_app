from django.shortcuts import render, redirect, get_object_or_404
from .models import Motor, Pelanggan, Transaksi, Motor, Pelanggan
from .forms import MotorForm, PelangganForm, TransaksiForm

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils import timezone

from django.utils.timezone import now


# Home
@login_required
def home(request):
    return render(request, 'rental/home.html')


@login_required
def dashboard(request):
    # Data motor
    total_motor = Motor.objects.count()
    tersedia = Motor.objects.filter(tersedia=True).count()
    tidak_tersedia = total_motor - tersedia

    # Data transaksi
    total_transaksi = Transaksi.objects.count()
    sudah_kembali = Transaksi.objects.filter(status_pengembalian=True).count()
    belum_kembali = total_transaksi - sudah_kembali

    # Data pelanggan berdasarkan status
    pelanggan_status = Pelanggan.objects.values('status').annotate(jumlah=Count('id'))
    status_labels = [item['status'] for item in pelanggan_status]
    status_counts = [item['jumlah'] for item in pelanggan_status]

    context = {
        'tersedia': tersedia,
        'tidak_tersedia': tidak_tersedia,
        'sudah_kembali': sudah_kembali,
        'belum_kembali': belum_kembali,
        'status_labels': status_labels,
        'status_counts': status_counts,
    }

    return render(request, 'rental/dashboard.html', context)

# ================== PDF ====================
@login_required
def export_pdf_transaksi(request):
    transaksi = Transaksi.objects.all()
    template = get_template('rental/pdf_transaksi.html')
    html = template.render({'data': transaksi})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="laporan_transaksi.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response

@login_required
def export_pdf_per_transaksi(request, pk):
    transaksi = get_object_or_404(Transaksi, pk=pk)
    template = get_template('rental/pdf_per_transaksi.html')
    html = template.render({'t': transaksi})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="transaksi_{transaksi.pk}.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response

# ================== MOTOR ====================
@login_required
def motor_list(request):
    data = Motor.objects.all()
    return render(request, 'rental/motor_list.html', {'data': data})

@login_required
def motor_create(request):
    form = MotorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('motor_list')
    return render(request, 'rental/form.html', {'form': form, 'title': 'Tambah Data Motor'})

@login_required
def motor_edit(request, pk):
    obj = get_object_or_404(Motor, pk=pk)
    form = MotorForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('motor_list')
    return render(request, 'rental/form.html', {'form': form, 'title': 'Edit Data Motor'})

@login_required
def motor_delete(request, pk):
    obj = get_object_or_404(Motor, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('motor_list')
    return render(request, 'rental/confirm_delete.html')


# ================== PELANGGAN ====================
@login_required
def pelanggan_list(request):
    data = Pelanggan.objects.all()
    return render(request, 'rental/pelanggan_list.html', {'data': data})

@login_required
def pelanggan_create(request):
    form = PelangganForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pelanggan_list')
    return render(request, 'rental/form.html', {'form': form, 'title': 'Tambah Data Pelanggan'})

@login_required
def pelanggan_edit(request, pk):
    obj = get_object_or_404(Pelanggan, pk=pk)
    form = PelangganForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('pelanggan_list')
    return render(request, 'rental/form.html', {'form': form, 'title': 'Edit Data Pelanggan'})

@login_required
def pelanggan_delete(request, pk):
    obj = get_object_or_404(Pelanggan, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('pelanggan_list')
    return render(request, 'rental/confirm_delete.html')


# ================== TRANSAKSI ====================
@login_required
def transaksi_list(request):
    query = request.GET.get('q')
    if query:
        data = Transaksi.objects.filter(pelanggan__nama__icontains=query)
    else:
        data = Transaksi.objects.all()
    return render(request, 'rental/transaksi_list.html', {'data': data, 'query': query})


@login_required
# def transaksi_create(request):
#     if request.method == 'POST':
#         form = TransaksiForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('transaksi_list')  # Tambahkan redirect setelah simpan
#     else:
#         form = TransaksiForm()
#     return render(request, 'rental/form.html', {'form': form, 'title': 'Tambah Data Transaksi'})

def transaksi_create(request):
    if request.method == 'POST':
        form = TransaksiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaksi_list')  # Ganti sesuai nama url kamu
    else:
        form = TransaksiForm()

    # Motor list dikirim ke template untuk JavaScript
    motor_list = Motor.objects.all()
    
    return render(request, 'rental/form.html', {
        'form': form,
        'motor_list': motor_list,
        'title': 'Tambah Transaksi',
    })

# def transaksi_create(request):
#     if request.method == 'POST':
#         form = TransaksiForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('transaksi_list')  # Sesuaikan dengan URL Anda
#     else:
#         form = TransaksiForm()

#     motor_list = Motor.objects.all()
#     return render(request, 'transaksi_form.html', {'form': form, 'motor_list': motor_list})

    

@login_required
# def transaksi_edit(request, pk):
#     transaksi = get_object_or_404(Transaksi, pk=pk)
#     if request.method == 'POST':
#         form = TransaksiForm(request.POST, instance=transaksi)
#         if form.is_valid():
#             form.save()
#             return redirect('transaksi_list')
#     else:
#         form = TransaksiForm(instance=transaksi)
#     return render(request, 'rental/form.html', {'form': form, 'title': 'Edit Data Transaksi'})

def transaksi_edit(request, pk):
    transaksi = get_object_or_404(Transaksi, pk=pk)
    if request.method == 'POST':
        form = TransaksiForm(request.POST, instance=transaksi)
        if form.is_valid():
            form.save()
            return redirect('transaksi_list')
    else:
        form = TransaksiForm(instance=transaksi)

    motor_list = Motor.objects.all()
    
    return render(request, 'rental/form.html', {
        'form': form,
        'motor_list': motor_list,
        'title': 'Edit Transaksi',
    })


@login_required
def transaksi_delete(request, pk):
    obj = get_object_or_404(Transaksi, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('transaksi_list')
    return render(request, 'rental/confirm_delete.html')

@login_required
def kembalikan_motor(request, pk):
    transaksi = get_object_or_404(Transaksi, pk=pk)
    transaksi.status_pengembalian = True
    transaksi.motor.tersedia = True
    transaksi.motor.save()
    transaksi.save()
    return redirect('transaksi_list')




