from django.urls import path
from django.conf.urls import url
from .views import GetPromo,GetAllPromos

urlpatterns = [
    path('promos/',GetAllPromos.as_view()),
    url(r'^promos/(?P<pk>\d+)/$',GetPromo.as_view()),
]