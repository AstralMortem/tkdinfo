from django.contrib import admin
from .models import Belt, Regulation


class BeltAdmin(admin.ModelAdmin):
    prepopulated_fields = {'kupslug': ['kup',]}

admin.site.register(Belt, BeltAdmin)
admin.site.register(Regulation)

