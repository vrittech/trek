from ..models import HolidayTrip
from ..serializers.holiday_trip_serializers import HolidayTripReadSerializers,HolidayTripWriteSerializers
from ..utilities.importbase import *

class HolidayTripViewsets(viewsets.ModelViewSet):
    serializer_class = HolidayTripReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = HolidayTrip.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return HolidayTripWriteSerializers
        return super().get_serializer_class()
    