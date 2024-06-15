from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Upload media gallery
class UploadMedia(models.Model):
    upload_user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.FileField(upload_to='media')
    img_bio = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.upload_user.username