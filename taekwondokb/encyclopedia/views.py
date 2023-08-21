from django.shortcuts import render
from .models import *


def toms(request):
    volume = Volume.objects.all()
    return render(request, 'tom.html', {'volume': volume})

def volume(request, volume):
    volume = Volume.objects.get(slug=volume)
    pages = Page.objects.filter(tom=volume)

    context = {'volume': volume, 'pages': pages, 'title': f"Том {volume.tom}"}

    return render(request, 'volume-detail.html',context )

def page(request,volume,page):
    page = Page.objects.get(tom__slug=volume, page=page)

    context = {'page': page}
    return render(request, 'page.html', context)

