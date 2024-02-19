"""
URL configuration for cnex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse

from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="Trek Ecommerce API",
      default_version='v1',
      description="Trek Ecommerce System",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="manojdas.py@gmail.com"),
      license=openapi.License(name="No License"),
      **{'x-logo': {'url': 'your-logo-url'}},
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path('', lambda request: HttpResponse("cdn storage fixing"), name='index'),
    path('api/accounts/',include('accounts.urls')),
    path('api/',include('blog.urls')),
    path('api/',include('booking.urls')),
    path('api/',include('holiday.urls')),
    path('api/',include('services.urls')),
    path('api/',include('managements.urls')),
    

    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
