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

class DonationCardForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=DonationCategory.objects.all(), widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = DonationCard
        fields = ['donation_title', 'total_cow_adopt', 'img']  

    def __init__(self, *args, **kwargs):
        super(DonationCardForm, self).__init__(*args, **kwargs)
        # You can set an initial category if required
        self.fields['category'].initial = DonationCategory.objects.first()  

class DonationForm(forms.ModelForm):
    amount_paid = forms.FloatField(required=True)
    custom_amount_paid = forms.FloatField(required=False)
    request_80g = forms.BooleanField(required=False)
    category = forms.ModelChoiceField(queryset=DonationCategory.objects.all(), widget=forms.HiddenInput(),required=False)


    class Meta:
        model = User
        fields = ['username', 'email', 'mobile']