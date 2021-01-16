from django.contrib import admin
from .models import OperatingSystem

class OperatingSystemAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'created_at', 'updated_at')
	search_fields = ('name', 'description',)

admin.site.register(OperatingSystem, OperatingSystemAdmin)
