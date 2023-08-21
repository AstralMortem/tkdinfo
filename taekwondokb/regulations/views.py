from django.shortcuts import render
from .models import Belt, Regulation

def belts(request):
    belts = Belt.objects.all()
    context = {
        'belts': belts,
        'title': 'Belts'
    }
    return render(request, 'belts.html', context)


def regulation(request, belt_kup):
    regulation = Regulation.objects.get(belt__kupslug = belt_kup)
    context = {
        'regulation': regulation,
        'title': regulation.belt.kup
    }
    return render(request, 'regulation.html', context)



