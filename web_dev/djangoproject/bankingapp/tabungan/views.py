from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from tabungan.forms import BukuTabunganForm
from tabungan.models import Buku, Transaksi

# Create your views here.
def list_buku(request):
    #query data ke db
    list_buku = Buku.objects.all() #mengambil semua data buku
    # print('lihat data buku:')
    # print(list_buku) #cek di terminal
    data = {'list_buku': list_buku}
    return render(request, "buku/list.html", data)


def create_buku(request):
    form = BukuTabunganForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tabungan:list-buku'))
    data ={}
    data['form'] = form
    return render(request, "buku/create.html", data)

def update_buku(request, buku_id):
    print(buku_id)
    object = get_object_or_404(Buku, id = buku_id)
    print(object)
    form = BukuTabunganForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tabungan:list-buku'))
    context = {}
    context['form'] = form
    return render(request, "buku/update.html", context)

def delete_buku(request, buku_id):
    # print(buku_id)
    object = get_object_or_404(Buku, id = buku_id)
    # print(object)
    if request.method == "POST":
        object.delete()
        return HttpResponseRedirect(reverse('tabungan:list-buku'))
    context = {'object': object}
    # object['object'] = object
    return render(request, "buku/delete.html", context)

def detail_transaksi(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    transaksi_list = Transaksi.objects.filter(buku=buku).order_by('-tanggal')
    
    # Hitung saldo
    saldo = 0
    for transaksi in transaksi_list.reverse():
        if transaksi.jenis == 'kredit':
            saldo += transaksi.nominal
        else:
            saldo -= transaksi.nominal
    
    context = {
        'buku': buku,
        'transaksi_list': transaksi_list,
        'saldo': saldo
    }
    return render(request, "buku/detail_transaksi.html", context)

def create_transaksi(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    if request.method == "POST":
        jenis = request.POST.get('jenis')
        nominal = request.POST.get('nominal')
        
        if jenis in ['debit', 'kredit'] and nominal:
            transaksi = Transaksi(buku=buku, jenis=jenis, nominal=nominal)
            transaksi.save()
            return HttpResponseRedirect(reverse('tabungan:detail-transaksi', args=[buku.id]))
    return render(request, "buku/create_transaksi.html", {'buku': buku})