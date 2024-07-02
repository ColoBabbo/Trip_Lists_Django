from django.contrib import admin
from .models import list, trip, item

# Register your models here.
admin.site.register(trip.Trip)
admin.site.register(list.List)
admin.site.register(item.Item)