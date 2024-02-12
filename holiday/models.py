from django.db import models
import uuid
from django.utils.text import slugify
   

# Create your models here.
class HolidayType(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    name = models.Model(max_length = 400,unique = True)
    slug = models.SlugField(unique = True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to="holiday/holiday_type_image/",null=True,blank=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Generate the slug when saving the holiday type if it's blank
        if not self.slug:
            self.slug = slugify(self.name)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)


class HolidayDestination(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length = 450)
    slug = models.SlugField(unique = True,blank=True)
    short_description = models.CharField(max_length = 450,blank = True,null = True)
    price = models.FloatField(null = True,blank = True)
    image = models.ImageField(upload_to="holiday/images/",null=True,blank=True)
    important_points = models.CharField(max_length = 450)
    stars = models.IntegerField(default = 4)
    trekking_difficulty = models.CharField(max_length = 450)
    stay_type = models.CharField(max_length = 450)
    activities = models.CharField(max_length = 450)


    description = models.TextField()
    map = models.URLField(null=True,blank=True)
    trip_information =  models.CharField(max_length = 450)
    ltinerary =  models.CharField(max_length = 450)
    weather =  models.CharField(max_length = 450)
    equipment =  models.CharField(max_length = 450)
    useful_information =  models.CharField(max_length = 450)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Generate the slug when saving the holiday type if it's blank
        if not self.slug:
            self.slug = slugify(self.title)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)


class HolidayDestinationHaveImages(models.Model):
    holiday_destination = models.ForeignKey(HolidayDestination,related_name = "images")
    image = models.ImageField(upload_to="holiday/images/",null=True,blank=True)


