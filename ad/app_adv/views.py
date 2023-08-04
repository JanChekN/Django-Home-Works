from django.shortcuts import render


# Create your views here.
def advertisement(reqest):
    return render(reqest, 'advertisement.html')


def advertisement_post(reqest):
    return render(reqest, 'advertisement-post.html')


def index(reqest):
    return render(reqest, 'index.html')


def login(reqest):
    return render(reqest, 'login.html')


def profile(reqest):
    return render(reqest, 'profile.html')


def register(reqest):
    return render(reqest, 'register.html')


def top_sellers(reqest):
    return render(reqest, 'top-sellers.html')
