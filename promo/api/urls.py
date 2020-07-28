from django.urls import path
from django.conf.urls import url
from .views import PromoAddApi,PromoModifyApi

urlpatterns = [
    path('add/',PromoAddApi.as_view()),
    url(r'^setup/(?P<pk>\d+)/$',PromoModifyApi.as_view()),
]