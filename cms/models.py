from django.db import models
from django.utils.text import slugify
from django.conf import settings

# Create your models here.

class HeroSectionContent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.FileField(upload_to='media/')
    images = models.JSONField(null=True, blank=True)  # Store image paths as JSON
    title =  models.CharField(max_length=250, null=True, blank=True)
    youtube_link = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    @property
    def image_list(self):
        return self.images if isinstance(self.images, list) else []


class DonationCategory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
   # slug = models.SlugField(unique=True, blank=True) 
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.category_name



class DonationCard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    donate_category = models.ForeignKey(DonationCategory, on_delete=models.CASCADE)
    img = models.FileField(upload_to='media/')
    donation_title = models.CharField(max_length=400, null=True, blank=True) 
    total_cow_adopt = models.BigIntegerField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.user.username
    

class DonatedPerson(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount_paid = models.FloatField()
    custome_amount_paid = models.FloatField(null=True, blank=True)
    donate_category = models.ForeignKey(DonationCategory, on_delete=models.CASCADE)
    donated_on_date = models.DateTimeField(auto_now=True)
    request_80g = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


