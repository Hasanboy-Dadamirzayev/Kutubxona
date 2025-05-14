
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kitoblar/', kitoblar),
    path('kitob/', kitob),
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
    path('talabalar/', talabalar_view, name='talabalar'),
    path('talabalar/<int:talaba_id>/', talaba_view),
    path('talabalar/<int:talaba_id>/delete', talaba_delete_view),
    path('mualliflar/', mualliflar, name='maulliflar'),
    path('mualliflar/<int:muallif_id>/delete', muallif_delete_view),
    path('mualliflar/<int:muallif_id>/edit', muallif_edit),
    path('mualliflar/create', mualliflar_from),
    path('recordlar/', recordlar, name='recordlar'),
    path('recordlar/<int:record_id>/', record_confirm),
    path('recordlar/<int:record_id>/delete', record_delete),
    path('recordlar/<int:record_id>/edit', record_edit),
    path('record_talabalar/', record_talabalar),
    path('recordlar/create', record_create),
    path('talabalar/<int:talaba_id>/update', talaba_update_view),
    path('adminlar/', adminlar, name='adminlar'),
    path('adminlar/<int:kutubxonachi_id>/', kutubxonachi),
    path('adminlar/<int:kutubxonachi_id>/delete', kutubxonachi_delete),
    path('adminlar/<int:kutubxonachi_id>/confirm', kutubxonachi_delete_confirm),
    path('adminlar/<int:kutubxonachi_id>/edit', kutubxonachi_edit),

]
