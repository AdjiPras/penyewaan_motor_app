from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('motor/', views.motor_list, name='motor_list'),
    path('motor/tambah/', views.motor_create, name='motor_create'),
    path('motor/edit/<int:pk>/', views.motor_edit, name='motor_edit'),
    path('motor/hapus/<int:pk>/', views.motor_delete, name='motor_delete'),

    path('pelanggan/', views.pelanggan_list, name='pelanggan_list'),
    path('pelanggan/tambah/', views.pelanggan_create, name='pelanggan_create'),
    path('pelanggan/edit/<int:pk>/', views.pelanggan_edit, name='pelanggan_edit'),
    path('pelanggan/hapus/<int:pk>/', views.pelanggan_delete, name='pelanggan_delete'),

    path('transaksi/', views.transaksi_list, name='transaksi_list'),
    path('transaksi/tambah/', views.transaksi_create, name='transaksi_create'),
    path('transaksi/edit/<int:pk>/', views.transaksi_edit, name='transaksi_edit'),
    path('transaksi/hapus/<int:pk>/', views.transaksi_delete, name='transaksi_delete'),

    path('transaksi/export/pdf/', views.export_pdf_transaksi, name='export_pdf_transaksi'),
    path('transaksi/kembalikan/<int:pk>/', views.kembalikan_motor, name='kembalikan_motor'),
    path('transaksi/pdf/<int:pk>/', views.export_pdf_per_transaksi, name='export_pdf_per_transaksi'),

]
