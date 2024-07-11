from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [

    path('', index, name='index'),

    path('upload_img', UploadImgGallery, name='upload_images'),

    path('get_gallery', get_gallery_data, name='get_gallery'),

    path('our_work',our_work, name='our_work'),

    path('trustee', trustee, name='trustee'),

    path('about', about, name='about'),

    path('gallery', gallery, name='gallery'),

    path('get_involved', get_involved, name='get_involved')
]