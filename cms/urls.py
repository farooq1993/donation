from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [

    path('dashboard', dashboard, name='dashboard'),
    path('herosection', herosection, name='herosection'),
    path('add_donation_category', add_donation_category , name='add_donation_category'),
    path('all_donation_cards', all_donationcards, name='all_donation_cards'),
    path('get_donationcard/<int:id>/',get_donationcard, name='get_donationcard'),
    path('donation_card',donation_card, name='donation_card'),
  
]