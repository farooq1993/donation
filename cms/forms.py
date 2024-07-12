from django import forms
from .models import HeroSectionContent


class HerosectionForm(forms.ModelForm):
    class Meta:
        model = HeroSectionContent
        fields = ['title'] 