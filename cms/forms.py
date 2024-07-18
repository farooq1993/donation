from django import forms
from .models import *
from users.models import User

class HerosectionForm(forms.ModelForm):
    class Meta:
        model = HeroSectionContent
        fields = ['title'] 


#Add category Form
class DonationCategoryAdd(forms.ModelForm):
    class Meta:
        model = DonationCategory
        fields = "__all__"
        exclude = ['user']


class DonationForm(forms.ModelForm):
    amount_paid = forms.FloatField()
    custom_amount_paid = forms.FloatField(required=False)
    request_80g = forms.BooleanField(required=False)
    category = forms.ModelChoiceField(queryset=DonationCategory.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile']