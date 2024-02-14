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
    
    def save(self, *args, **kwargs):
        # Generate the slug when saving the holiday type if it's blanks
        if not self.slug:
            self.slug = slugify(self.name)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)