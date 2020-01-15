from django.contrib import admin

# from __future__ import unicode_literals
from .models import MwendaShop



# Register your models here.

class MwendaShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description', 'price')

admin.site.register(MwendaShop, MwendaShopAdmin)
