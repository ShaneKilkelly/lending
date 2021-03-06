from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    prepopulated_fields = { 'slug': ("name",) }

admin.site.register(Item, ItemAdmin)
