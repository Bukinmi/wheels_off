from django.contrib import admin
from .models import Meetups, Location, Participant

# Register your models here.
admin.site.register(Meetups)
admin.site.register(Location)
admin.site.register(Participant)