from django.contrib import admin
from api.models import Location, LocationParking, LocationStat


class LocationAdmin(admin.ModelAdmin):
    search_fields = ('id', 'location_name', 'sub_location', 'floor')
    list_display = ('id', 'location_name', 'sub_location',
                    'floor', 'max_capacity')


admin.site.register(Location, LocationAdmin)


class LocationParkingAdmin(admin.ModelAdmin):
    search_fields = ('id', 'location_name', 'sub_location', 'floor')
    list_display = ('id', 'location_name', 'sub_location',
                    'floor', 'available')


admin.site.register(LocationParking, LocationParkingAdmin)
