from django.http import HttpResponse
from django.shortcuts import render
from .models import Trip, List, Item
from pprint import pprint

# Create your views here.
def index(request):
    context = {
        'special_message': "Now I've got context"
    }
    return render(request, 'index.html', context)

def all_trips(request):
    all_trips = Trip.objects.all()
    context = {'all_trips' : all_trips}
    return render(request, 'trips/show_all_trips.html', context)

def add_trip(request):
    return HttpResponse('Add a New Trip')

def show_trip(request, trip_id):
    this_trip = Trip.objects.get(id=trip_id)
    context = {"trip_id":trip_id, "this_trip" : this_trip, }
    return render(request, 'trips/show_one_trip.html', context)

def show_list(request, trip_id, list_id):
    response = "Packing List %s"
    return HttpResponse(response % trip_id, list_id)

def show_item(request, trip_id, list_id, item_id):
    response = "Item %s detail view "
    return HttpResponse(response % [trip_id, list_id, item_id])