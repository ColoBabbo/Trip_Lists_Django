from django.urls import path

from . import views

app_name = "trips"
urlpatterns = [
    path("", views.all_trips,  name = "all_trips"),
    path("index", views.index, name = "index"),
    path("trip/", views.add_trip, name='add_trip'),
    path("trip/<int:trip_id>", views.show_trip, name='show_trip'),
    path("trip/<int:trip_id>/list/<int:list_id>", views.show_list, name='show_list'),
    path("trip/<int:trip_id>/list/<int:list_id>/item/<int:item_id>", views.show_item, name='show_item'),
]