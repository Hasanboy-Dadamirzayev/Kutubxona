
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mualliflar/', mualliflar),
    path('muallif1/', muallif1),
    path('kitoblar/', kitoblar),
    path('kitob/', kitob),
    path('recordlar/', recordlar),
    path('tirik', tirik),
    path('eng_katta/', eng_katta),
    path('kitobi_kop/', kitobi_kop),
    path('olinga_sana', olingan_sana),
    path('tirik_kitob/', tirik_kitob),
    path('badiiy/', baddiy),
    path('katta_mualliflar/', katta_mualliflar),
    path('kitob_soni/', kitob_soni),
    path('tanlangan_record/', tanlangan_record),
    path('bitiruvchi_recordlar', bitiruvchi_recordlar),
]
