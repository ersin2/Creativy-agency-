from django.contrib import admin

# Register your models here.
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ("title",)}

admin.site.register(Service, ServiceAdmin)