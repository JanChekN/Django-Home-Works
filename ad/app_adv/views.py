from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .forms import AdvertisementForm
from .models import Advertisement


# Create your views here.
def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {
        'advertisement': advertisement
    }
    return render(request, 'app_adv/advertisement.html', context)

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(reqest):
    if reqest.method == 'POST':
        form = AdvertisementForm(reqest.POST, reqest.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = reqest.user
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(reqest, 'app_adv/advertisement-post.html', context)


def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements, 'title': title}
    return render(request, 'app_adv/index.html', context)





def profile(reqest):
    return render(reqest, 'app_auth/profile.html')


def register(reqest):
    return render(reqest, 'app_auth/register.html')


def top_sellers(reqest):
    return render(reqest, 'app_adv/top-sellers.html')
