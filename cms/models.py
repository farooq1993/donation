from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField
from django.conf import settings

# Create your models here.

class HeroSectionContent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.FileField(upload_to='media/')
    images = models.JSONField(null=True, blank=True)  # Store image paths as JSON
    title =  models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    @property
    def image_list(self):
        return self.images if isinstance(self.images, list) else []


class DonationCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Donation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    donate_category = models.ForeignKey(DonationCategory, on_delete=models.CASCADE)
    donation_title = RichTextField()
    total_cow_adopt = models.BigIntegerField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.donation_title


