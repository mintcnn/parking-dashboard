from django.contrib import admin
from api.models import Location, LocationParking, LocationStat


class LocationAdmin(admin.ModelAdmin):
    search_fields = ('id', 'location_name', 'sub_location', 'floor')
    list_display = ('id', 'location_name', 'sub_location',
                    'floor', 'max_capacity')


admin.site.register(Location, LocationAdmin)


class LocationParkingAdmin(admin.ModelAdmin):
    search_fields = ('id', 'location__id', 'location__location_name', 'location__sub_location' )
    list_display = ('id', 'location', 'available')
    raw_id_fields = ('location',)


admin.site.register(LocationParking, LocationParkingAdmin)


class LocationStatAdmin(admin.ModelAdmin):
    search_fields = ('id', 'location__id', 'location__location_name', 'location__sub_location' )
    list_display = ('id', 'location', 'day_of_week', 'datetime', 'available')
    raw_id_fields = ('location',)


admin.site.register(LocationStat, LocationStatAdmin)
