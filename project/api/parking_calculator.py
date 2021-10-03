from api.models import Location, LocationParking, LocationStat
from django.db.models import F


def edit_location_parking(data):
    try:
        location = Location.objects.get(id=data['id'])
    except Location.DoesNotExist:
        return False

    location_parking, created = LocationParking.objects.get_or_create(
        id=data['id'],
        defaults={
            'location_name': location.location_name,
            'sub_location': location.sub_location,
            'floor': location.floor,
            'available': location.max_capacity - data['parking_change'],
        }
    )
    if not created:
        location_parking.available = location_parking.available - \
            data['parking_change']
        if location_parking.available > location.max_capacity:
            location_parking.available = location.max_capacity
        location_parking.save()

    return True


def stat_location():
    return True
