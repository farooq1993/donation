from django.db import models
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


