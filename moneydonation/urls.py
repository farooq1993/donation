from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('login', LoginView, name='login'),
    path('upload_img', UploadImgGallery, name='upload_images'),
    path('get_gallery', get_gallery_data, name='get_gallery')
]