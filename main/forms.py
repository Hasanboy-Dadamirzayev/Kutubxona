from django import forms
from .models import *

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = '__all__'

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
