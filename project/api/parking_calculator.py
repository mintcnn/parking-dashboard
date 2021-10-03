from api.models import Location, LocationParking, LocationStat
import pendulum

day_of_week_mapping={
    '0': 'Sun',
    '1': 'Mon',
    '2': 'Tue',
    '3': 'Wed',
    '4': 'Thu',
    '5': 'Fri',
    '6': 'Sat'
}

def edit_location_parking(data):
    try:
        location = Location.objects.get(id=data['id'])
    except Location.DoesNotExist:
        return False

    location_parking, created = LocationParking.objects.get_or_create(
        location=location,
        defaults={
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


def stat_location(data):
    try:
        location = Location.objects.get(id=data['id'])
        location_parking = LocationParking.objects.get(location=location)
    except Location.DoesNotExist:
        return False
    dt = pendulum.now(tz='Asia/Bangkok')
    LocationStat.objects.create(
        location=location,
        day_of_week=day_of_week_mapping[str(dt.day_of_week)],
        available=location_parking.available,
    )
    return True
