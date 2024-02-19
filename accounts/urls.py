from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import LoginView
from rest_framework.routers import DefaultRouter
from .views import PermissionAllDelete,RoleViewSet,CheckTokenExpireView,userLimitedData,AllUserData
from .group_permission import PermissionHasGroupViewSet,CustomPermissionInsert

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = DefaultRouter()

router.register('users', views.CustomUserSerializerViewSet, basename="CustomUserSerializer")

# router.register('groups', views.GroupViewSet, basename="group")
# router.register('permissions', views.PermissionViewSet, basename="permission")

# router.register("permission-has-group",PermissionHasGroupViewSet,basename="PermissionHasGroupViewSet")


urlpatterns = [    
    path('auth/login/', LoginView.as_view()),
    path('', include(router.urls)),

    path('gettoken/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('refresh-token',TokenRefreshView.as_view(),name = 'refresg-token'),
    path('token-verify/',TokenVerifyView.as_view(),name="token_verify"),

    path('check-token-status/',CheckTokenExpireView.as_view(),name="token_verify"),
    path('roles/',RoleViewSet.as_view()),

    path('add-customized-permission/',CustomPermissionInsert,name="CustomPermissionInsert"),

    # path('get-limited-user-data/',userLimitedData.as_view(),name="userLimitedData"),
    # path('get-all-users-data/',AllUserData.as_view(),name="userLimitedData"),
    
    # path('user-details/<str:username>/', views.UserDetailsView.as_view(), name="user_details"),

    path('google-login/', views.GoogleLogin.as_view(), name="user_details"),
    # path('user-has-groups/',)
]