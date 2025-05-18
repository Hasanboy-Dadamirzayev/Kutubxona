from django.contrib import admin
from .models import *


class KutubxonachiAdmin(admin.ModelAdmin):
    list_filter = ['ish_vaqti']
    search_fields = ['ism']
    search_help_text = "Ism boyicha qidirish"

class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1

class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'jins', 'tugilgan_sana', 'kitob_soni', 'tirik')
    inlines = (KitobInline,)
    list_display_links = ('id', 'ism')
    list_editable = ('kitob_soni', 'tirik')
    search_fields = ['ism']
    list_filter = ['tirik']


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'talaba', 'kitob', 'admin', 'olingan_sana', 'qaytarish_sana', 'qaytarilgan')
    list_editable = ['qaytarilgan']
    list_display_links = ('id', 'talaba')
    search_fields = ('talaba__ism', 'kitob__nom', 'admin__ism')






admin.site.register(Admin, KutubxonachiAdmin,)
admin.site.register(Kitob)
admin.site.register(Talaba)
admin.site.register(Muallif, MuallifAdmin,)
admin.site.register(Record, RecordAdmin,)
