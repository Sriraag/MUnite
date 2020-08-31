from django.contrib import admin

# Register your models here.
from .models import Delegate, Event

admin.site.register(Delegate)
admin.site.register(Event)