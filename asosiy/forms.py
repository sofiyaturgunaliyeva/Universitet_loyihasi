from .models import *
from django import forms

# Vazifa
# 4-topshiriq: Universitet loyihasida Fan qo’shishni django form orqali qayta bajaring.

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = '__all__'

# 5-topshiriq . Yo’nalish qo’shishni django form orqali qayta bajaring.

class YonalishForm(forms.Form):
    nom = forms.CharField()
    aktivligi = forms.BooleanField()


# 6-topshiriq. Ustoz qo’shishni django form orqali qayta bajaring

class UstozForm(forms.ModelForm):
    class Meta:
        model = Ustoz
        fields = '__all__'