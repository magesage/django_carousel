from django.contrib import admin
from .models import slide

# Register your models here.
class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'url', 'alt')
    list_display_links = ('id', 'caption', 'alt')

admin.site.register(slide, SlideAdmin)