import django
from django.shortcuts import render, redirect, HttpResponse
from .models import Player
from .forms import PlayerForm

def mainpage(request):
    context = {
        'page_title': 'Mainpage',
        'player_name': 'player',
    }
    return render(request, "mainpage.html", context)

def mainpage_redirect(request):
    if request.method == 'GET':
        return redirect('mainpage')
    else:
        return HttpResponse(f"Bad method for this endpoint: GET was expected.", status=400)

def registration(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mainpage')
    elif request.method == 'GET':
        form = PlayerForm()
        players = Player.objects.all()
        return render(request, 'registration.html', {'form': form, 'players': players})
    else:
        return HttpResponse(f"Bad method for this endpoint: GET or POST was expected.", status=400)