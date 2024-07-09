from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


# Upload media gallery
class UploadMedia(models.Model):
    upload_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.FileField(upload_to='uploads/')
    images = models.JSONField(null=True, blank=True)  # Store image paths as JSON
    img_bio = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.upload_user.username