from rest_framework import (
    serializers,
    fields
)


class PostParkingSerializer(serializers.Serializer):
    id = fields.IntegerField(required=True, min_value=1)
    parking_change = fields.IntegerField(required=True)
    datetime = fields.DateTimeField(required=True)
