from django.urls import path
from .views import LoginApiView

urlpatterns = [
    path('login/',LoginApiView.as_view()),
]