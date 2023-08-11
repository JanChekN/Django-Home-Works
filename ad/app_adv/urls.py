from django.urls import path

from .views import *

urlpatterns = [
    path('advertisement/', advertisement, name='advertisement'),
    path('advertisement_post/', advertisement_post, name='advertisement_post'),
    path('', index, name='main-page'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('top_sellers/', top_sellers, name='top-sellers'),

]
