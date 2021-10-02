from api.serializers import PostParkingSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated


class EditParkingLotView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        serializer = PostParkingSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={
                    'errors': serializer.errors,
                    'code': status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data

        return Response(
            data={
                'message': 'edit parking lot success',
                'code': status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )

    def edit_location_parking(self):
        return True

    def stat_location(self):
        return True
