from django.urls import path
from .views import LoginApiView,ChangePassword
from knox.views import LogoutView

urlpatterns = [
    path('login/',LoginApiView.as_view(),name='Login'),
    path('logout/',LogoutView.as_view(),name='Logout'),
    path('changepassword/',ChangePassword.as_view(),name='Change Password'),
]