from django.shortcuts import render
from django.http import HttpResponse
from main.models import *

from main.models import *

def mualliflar(request):
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar
    }
    return render(request, 'mualliflar.html', context)

def muallif1(request):
    muallif = Muallif.objects.get(id=1)
    context = {
        'muallif': muallif
    }
    return render(request, 'muallif1.html', context)

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

def recordlar(request):
    recordlar = Record.objects.all()
    context = {
        'recordlar': recordlar
    }
    return render(request, 'recordlar.html', context)

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