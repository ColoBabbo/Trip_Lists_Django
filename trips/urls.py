from django.urls import path

from . import views

urlpatterns = [
    path("", views.all_trips,  name = "all_trips"),
    path("index", views.index, name = "index"),

    path("<int:trip_id>", views.show_trip, name='show_trip'),

    path("list/<int:packing_list_id>", views.show_packing_list, name='show_packing_list'),
    path("list/<int:packing_list_id>/item/<int:item_id>", views.show_item, name='show_item'),
]