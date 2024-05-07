from django.contrib import admin

from .models import Team, SocialMedia


class SocialMediaInlineAdmin(admin.TabularInline):
    model = SocialMedia
    extra = 4

class TeamAdmin(admin.ModelAdmin):
    list_display = ['title', 'age', 'position', 'phone', 'image_tag']
    inlines = [SocialMediaInlineAdmin]
    prepopulated_fields = {'slug': ("title",)}

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['team', 'link']


admin.site.register(Team, TeamAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)