from django.contrib import admin
from django.db import models
from django.db.models.base import Model
from .models import Card

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = ('title','description',)

admin.site.register(Card,CardAdmin)