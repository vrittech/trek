from django.db import models
import uuid
from django.utils.text import slugify
# Create your models here.
class Question(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    question_title = models.CharField(max_length = 450)
    status = models.BooleanField(default = True)
    position = models.PositiveIntegerField(default = 999)
    
    def __str__(self):
        return self.title
    
class QuestionHaveAnswer(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    answer_title = models.CharField(max_length = 450)
    status = models.BooleanField(default = True)
    position = models.PositiveIntegerField(default = 1)
    question = models.OneToOneField(Question,related_name = "answer",on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.position = int(Testonomial.objects.last().position)+1
        super().save(*args, **kwargs)
    

class SiteSetting(models.Model):
    number = models.CharField(max_length = 150,blank=True,default = '')
    email = models.CharField(max_length = 150,blank=True,default = '')
    teliphone = models.CharField(max_length = 150,blank=True,default = '')
    contact_info = models.CharField(max_length = 150,blank=True,default = '')
    description = models.CharField(max_length = 150,blank=True,default = '')

    facebook = models.CharField(max_length = 150,blank=True,default = '')
    twitter = models.CharField(max_length = 150,blank=True,default = '')
    youtube = models.CharField(max_length = 150,blank=True,default = '')
    site_icon = models.ImageField(upload_to="site/images",null=True,blank=True)
    logo =  models.ImageField(upload_to="site/images",null=True,blank=True)
    site_title = models.CharField(max_length = 150,blank=True,default = '')
    site_name = models.CharField(max_length = 150,blank=True,default = '')
    
  
    def __str__(self):
        return self.site_name
    
class Testonomial(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length = 150,blank=True,default = '')
    description = models.CharField(max_length = 150,blank=True,default = '')
    content = models.TextField(blank=True,default = '')
    page_type = models.CharField(max_length=20,choices = (('normal','Normal'),('navbar_page','Navbar Page'),('footer_page','Footer Page')) ) #normal means should display in body anywhere ,navbar page is display as navbar
    first_images =  models.ImageField(upload_to="testonomial/images",null=True,blank=True)
    second_images =  models.ImageField(upload_to="testonomial/images",null=True,blank=True)

    place = models.PositiveIntegerField(default = 1)
    position = models.PositiveIntegerField(default = 1)
    
    def __str__(self):
        return self.site_name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.place  =  int(Testonomial.objects.last().place)+1
            self.position = int(Testonomial.objects.last().position)+1
        super().save(*args, **kwargs)
    
