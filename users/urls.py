from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [

    path('createuser', createuser, name='index'),
    path('login', LoginView, name='login'),
    path('donate/<int:category_id>/', donate, name='donate'),
    path('logout', LogoutView, name='logout'),

  
]