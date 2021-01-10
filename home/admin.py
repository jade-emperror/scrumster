from django.contrib import admin

# Register your models here.
from .models import load

admin.site.register(load)