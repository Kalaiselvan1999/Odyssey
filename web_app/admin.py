from django.contrib import admin
from .models import User, Odyssey, Requests, State

# Register your models here.

admin.site.register(User)
admin.site.register(Odyssey)
admin.site.register(Requests)
admin.site.register(State)
