from django.db import models
from accounts.models  import CustomUser
from holiday.models import HolidayDestination
from services.models import Services
import uuid

# Create your models here.

class TripBook(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    user = models.ForeignKey(CustomUser,related_name = 'trips', on_delete  = models.CASCADE)
    holiday_destination = models.ForeignKey(HolidayDestination,related_name = 'trips', on_delete = models.CASCADE)
    companions = models.CharField(max_length = 20,choices = [('solo'),('group')])
    number_of_persons = models.IntegerField(default = 1) #if group companions then specify numbers


class ServiceBook(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    user = models.ForeignKey(CustomUser,related_name = 'trips', on_delete  = models.CASCADE)
    services = models.ForeignKey(Services,related_name = 'trips', on_delete = models.CASCADE)
    
    