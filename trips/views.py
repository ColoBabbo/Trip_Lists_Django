from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'special_message': "Now I've got context"
    }
    return render(request, 'index.html', context)

def all_trips(request):
    return HttpResponse('All Trips Here')

def show_trip(request, trip_id):
    return HttpResponse("This is Trip %s" % trip_id)

def show_packing_list(request, packing_list_id):
    response = "Packing List %s"
    return HttpResponse(response % packing_list_id)

def show_item(request, packing_list_id, item_id):
    response = "Item %s detail view "
    return HttpResponse(response % item_id, packing_list_id)