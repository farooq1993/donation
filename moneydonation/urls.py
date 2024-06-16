from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='health_api'),
    path('login', LoginView, name='login'),
    path('upload_img', UploadImgGallery, name='upload_images'),
]