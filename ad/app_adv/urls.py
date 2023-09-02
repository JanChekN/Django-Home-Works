from django.urls import path

from .views import *

urlpatterns = [
    path('advertisement/<int:pk>', advertisement_detail, name='adv-detail'),
    path('advertisement_post/', advertisement_post, name='advertisement_post'),
    path('', index, name='main_page'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('top_sellers/', top_sellers, name='top_sellers'),

]
