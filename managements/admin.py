from django.contrib import admin
from .models import Question,QuestionHaveAnswer,Testonomial

# Register your models here.
admin.site.register([Question,QuestionHaveAnswer,Testonomial])
