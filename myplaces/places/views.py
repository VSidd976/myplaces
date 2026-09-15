from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import PlaceForm
from datetime import datetime
import random

# Create your views here.

def home(request):
    if 'places' not in request.session:
        request.session['places'] = []

    places = request.session['places']
    random_place = None

    if 'pick_random' in request.GET and places:
        weights = [int(p['rating']) for p in places]
        random_place = random.choices(places, weights=weights, k=1)[0]

    return render(request, 'places/home.html', {
        'random_place': random_place,
        'has_places': len(places) > 0
    })

def place_list(request):
    if 'places' not in request.session:
        request.session['places'] = []

    return render(request, 'places/place_list.html', {
        'places': request.session['places']
    })

def place_detail(request, place_id):
    places = request.session.get('places', [])
    place = next((p for p in places if p['id'] == place_id), None)
    if not place:
        raise Http404("Місце не знайдено")

    return render(request, 'places/place_detail.html', {'place': place})

def add_place(request):
    if 'places' not in request.session:
        request.session['places'] = []

    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            places = request.session['places']

            if not places:
                next_id = 1

            else:
                next_id = max(p['id'] for p in places) + 1

            new_item = {
                'id': next_id,
                'title': form.cleaned_data['title'],
                'place_type': form.cleaned_data['place_type'],
                'location': form.cleaned_data['location'].strip(),
                'rating': form.cleaned_data['rating'],
                'description': form.cleaned_data['description'],
                'created_at': datetime.now().strftime('%d.%m.%Y %H:%M'),
            }
        
            places.append(new_item)
            request.session['places'] = places

            return HttpResponseRedirect(reverse('places:list'))

        else:
            return render(request, 'places/place_form.html', {
                'form': form
            })

    return render(request, 'places/place_form.html')
