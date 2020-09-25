from django.urls import path
from django.conf.urls import url
from .views import GetProfessor,GetAllProfessors,RegisterProfessor,ProjectSubmission \
    ,ProjectUpdateDelete

urlpatterns = [
    path('professor/',GetAllProfessors.as_view()),
    url(r'^professor/(?P<pk>\d+)/$',GetProfessor.as_view()),
    path('register/',RegisterProfessor.as_view()),
    path('addproject/',ProjectSubmission.as_view()),
    url(r'^project/(?P<pk>\d+)/$',ProjectUpdateDelete.as_view()),

]