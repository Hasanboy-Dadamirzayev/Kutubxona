from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import *

from main.models import *


def kitoblar(request):
    kitoblar = Kitob.objects.all()
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'kitoblar.html', context)

def kitob(request):
    kitob = Kitob.objects.get(id=1)
    context = {
        'kitob': kitob
    }
    return render(request, 'kitob.html', context)


def tirik(request):
    tirik_mualliflar = Muallif.objects.filter(tirik=True)
    context = {
        'tirik_mualliflar': tirik_mualliflar
    }
    return render(request, 'tirik.html', context)

def eng_katta(request):
    kitoblar = Kitob.objects.order_by('sahifa')[:3]
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'sahifa.html', context)

def kitobi_kop(request):
    kitobi_kop_mualliflar = Muallif.objects.order_by('kitob_soni')[:3]
    context = {
        'kitobi_kop_mualliflar': kitobi_kop_mualliflar
    }
    return render(request, 'kitobi_kop_mualliflar.html', context)

def olingan_sana(request):
    olingan_sana = Record.objects.order_by('olingan_sana')[:3]
    context = {
        'olingan_sana': olingan_sana
    }
    return render(request, 'olingan_sana.html', context)

def tirik_kitob(request):
    kitoblar = Kitob.objects.filter(muallif__tirik=True)
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'tirik_kitob.html', context)

def baddiy(request):
    kitoblar = Kitob.objects.filter(janr='badiiy')
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'badiiy.html', context)

def katta_mualliflar(request):
    mualliflar = Muallif.objects.order_by('tugilgan_sana')[:3]
    context = {
        'mualliflar': mualliflar
    }
    return render(request, 'katta_mualliflar.html', context)

def kitob_soni(request):
    kitoblar = Kitob.objects.filter(muallif__kitob_soni__lt=10)
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'kitob_soni.html', context)

def tanlangan_record(request):
    record = Record.objects.get(id=1)
    context = {
        'record': record
    }
    return render(request, 'tanlangan_record.html', context)

def bitiruvchi_recordlar(request):
    recordlar = Record.objects.filter(talaba__kurs=4)
    context = {
        'recordlar': recordlar
    }
    return render(request, 'bitiruvchi_recordlar.html', context)

def talabalar_view(request):
    talabalar = Talaba.objects.all()
    context = {
        'talabalar': talabalar
    }
    return render(request, 'talabalar_view.html', context)

def talaba_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba
    }
    return render(request, 'talaba_view.html', context)

def talaba_delete_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    talaba.delete()
    return redirect('talabalar')

def mualliflar(request):
    mualliflar = Muallif.objects.all()

    search = request.GET.get('search')
    if search:
        mualliflar = Muallif.objects.filter(ism__contains=search)


    context = {
        'mualliflar': mualliflar,
        'search': search
    }
    return render(request, 'mualliflar.html', context)

def muallif_delete_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    muallif.delete()
    return redirect('maulliflar')

def recordlar(request):
    recordlar = Record.objects.all()
    context = {
        'recordlar': recordlar,
        'talalar': Talaba.objects.all(),
        'kitoblar': Kitob.objects.all(),
        'adminlar': Admin.objects.all(),
    }
    return render(request, 'recordlar.html', context)

def record_create(request):
    if request.method == 'POST':
        Record.objects.create(
            talaba = Talaba.objects.get(id=request.POST.get('talaba')),
            kitob = Kitob.objects.get(id=request.POST.get('kitob')),
            admin = Admin.objects.get(id=request.POST.get('admin')),
            olingan_sana = request.POST.get('olingan_sana'),
            qaytarish_sana = request.POST.get('qaytarish_sana'),
            qaytarilgan = True if request.POST.get('qaytarilgan') == 'on' else False
        )
        return redirect('recordlar')

    context = {
        'talabalar': Talaba.objects.all(),
        'kitoblar': Kitob.objects.all(),
        'adminlar': Admin.objects.all(),
    }
    return render(request, 'record_create.html', context)


def record_delete(request, record_id):
    record = Record.objects.get(id=record_id)
    record.delete()
    return redirect('recordlar')

def record_confirm(request, record_id):
    record = Record.objects.get(id=record_id)
    context = {
        'record': record
    }
    return render(request, 'record_confirm.html', context)

def record_talabalar(request):
    recordlar = Record.objects.all()

    search=request.GET.get('search')
    if search is not None:
        recordlar = Record.objects.filter(talaba__ism__contains=search)

    context = {
        'recordlar': recordlar,
        'search': search
    }
    return render(request, 'record_talabalar.html', context)

def mualliflar_from(request):
    if request.method == 'POST':
        Muallif.objects.create(
            ism = request.POST.get('ism'),
            jins = request.POST.get('jins'),
            tugilgan_sana = request.POST.get('tugilgan_sana'),
            kitob_soni = request.POST.get('kitob_soni'),
            tirik = True if request.POST.get('tirik') == 'on' else False
        )
        return redirect('maulliflar')
    return render(request, 'create_maullif.html')

def adminlar(request):
    if request.method == 'POST':
        Admin.objects.create(
            ism = request.POST.get('ism'),
            ish_vaqti = request.POST.get('ish_vaqti')
        )
        return redirect('adminlar')
    adminlar = Admin.objects.all()
    context = {
        'adminlar': adminlar
    }
    return render(request, 'adminlar.html', context)
