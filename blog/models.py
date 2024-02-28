from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length = 150,blank=True,default = '')
    description = models.CharField(max_length = 150,blank=True,default = '')
    contents = models.TextField(blank=True,default = '')
    image = models.ImageField(upload_to="site/images",null=True,blank=True)
  
    def __str__(self):
        return self.title
    