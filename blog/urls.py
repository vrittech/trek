from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import blog_viewsets

router = DefaultRouter()

router.register('users', blog_viewsets.BlogViewSets, basename="CustomUserSerializer")

urlpatterns = [    
    path('', include(router.urls)),
]