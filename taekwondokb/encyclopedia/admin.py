from django.contrib import admin
from .models import *



class VolumeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tom",)}  

admin.site.register(Volume, VolumeAdmin)
admin.site.register(Page)

