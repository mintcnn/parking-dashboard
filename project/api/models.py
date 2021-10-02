from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=255, null=False, blank=False)
    lattitude = models.CharField(max_length=50, null=False, blank=False)
    longitude = models.CharField(max_length=50, null=False, blank=False)
    max_capacity = models.IntegerField(null=False, blank=False)
    sub_location = models.CharField(max_length=255, null=False)
    floor = models.IntegerField()


class Location_parking(models.Model):
    sub_location = models.CharField(max_length=255, null=False)
    floor = models.IntegerField()
    available = models.IntegerField(null=False)


class Location_stat(models.Model):
    sub_location = models.CharField(max_length=255, null=False)
    floor = models.IntegerField()
    day_of_week = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
