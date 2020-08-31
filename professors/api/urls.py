from django.urls import path
from django.conf.urls import url
from .views import GetProfessor,GetAllProfessors,RegisterProfessor,ProjectSubmission

urlpatterns = [
    path('professor/',GetAllProfessors.as_view()),
    url(r'^professor/(?P<pk>\d+)/$',GetProfessor.as_view()),
    path('register/',RegisterProfessor.as_view()),
    path('add/',ProjectSubmission.as_view()),
]