from django.urls import path
from django.conf.urls import url
from .views import GetProfessor,GetAllProfessors

urlpatterns = [
    path('professor/',GetAllProfessors.as_view()),
    url(r'^professor/(?P<pk>\d+)/$',GetProfessor.as_view()),
]