from django.urls import path
from custom.views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user-profile/', UserProfileView.as_view(), name='user-profile'),
    path('site-setting/', SiteSettingView.as_view(), name='site-setting'),
    path('login/', CustomLoginView.as_view(), name='custom-login'),
    path('verify-login-email/', VerifyLoginEmailView.as_view(), name='verify-login-email'),
    path('user-time-zone/', UserTimeZoneView.as_view(), name='user-time-zone'),
]