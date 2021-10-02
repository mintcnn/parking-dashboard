from django.contrib import admin
from api.models import Location


class LocationAdmin(admin.ModelAdmin):
    search_fields = ('id', 'location_name', 'sub_location', 'floor')
    list_display = ('id', 'location_name', 'sub_location',
                    'floor', 'max_capacity')


admin.site.register(Location, LocationAdmin)
