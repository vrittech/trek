from ..models import HolidayType
from ..serializers.holiday_type_serializers import HolidayTypeReadSerializers,HolidayTypeWriteSerializers
from ..utilities.importbase import *

class HolidayTypeViewsets(viewsets.ModelViewSet):
    serializer_class = HolidayTypeReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = HolidayType.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return HolidayTypeWriteSerializers
        return super().get_serializer_class()
    