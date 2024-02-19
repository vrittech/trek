from django.urls import path, include
from rest_framework.routers import DefaultRouter
from viewsets import site_setting_viewsets,testonomial_viewsets

router = DefaultRouter()

router.register('gite-setting', site_setting_viewsets.SiteSettingViewsets, basename="SiteSettingViewsets")
router.register('holiday-trip-type', testonomial_viewsets.TestonomialViewsets, basename="TestonomialViewsets")

urlpatterns = [    
    path('', include(router.urls)),
]