from django import forms
from .models import Sezon, Razm

class SezonForm(forms.ModelForm):
    name = forms.CharField(label='Название')
    class Meta:
        model = Sezon
        fields = '__all__'

class RazmerForm(forms.ModelForm):
    name = forms.CharField(label='Название')
    class Meta:
        model = Razm
        fields = '__all__'
