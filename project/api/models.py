from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=255, null=False, blank=False)
    lattitude = models.CharField(max_length=50, null=False, blank=False)
    longitude = models.CharField(max_length=50, null=False, blank=False)
    max_capacity = models.IntegerField(null=False, blank=False)
    sub_location = models.CharField(max_length=255, null=False)
    floor = models.CharField(max_length=10, null=False)


class LocationParking(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    available = models.IntegerField(null=False)


class LocationStat(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=50, null=False, blank=False)
    datetime = models.DateTimeField(auto_now=False)
    available = models.IntegerField(null=False)
