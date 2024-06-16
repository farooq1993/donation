# import form class from django
from django import forms
 
# import from models.y
from .models import UploadMedia

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadMedia
        fields = ['img_bio']