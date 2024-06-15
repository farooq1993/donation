from django.contrib import admin
from .models import UploadMedia
# Register your models here.


@admin.register(UploadMedia)
class UploadmediaAdmin(admin.ModelAdmin):
    list_display = ('upload_user', 'img', 'img_bio', 'uploaded_at', 'updated_at')