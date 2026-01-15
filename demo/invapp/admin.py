from django.contrib import admin

# Register your models here.

from .models import Tuote, Varastot

admin.site.register(Tuote)
admin.site.register(Varastot)