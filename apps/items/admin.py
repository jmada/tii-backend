from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display = ('description', 'serial_number', 'image', 'created_at', 'updated_at')
	search_fields = ('description',)

admin.site.register(Item, ItemAdmin)
