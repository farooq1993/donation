from django.urls import path
from .views import *

urlpatterns = [

    path('', health_api.as_view(), name='health_api'),
    path('login', LoginView.as_view(), name='login'),
    path('upload_img', UploadImgGallery.as_view(), name='upload_images'),
]