from django.urls import path
from django.conf.urls import url
from .views import GetStudent,GetAllStudents,RegisterStudent,CreateTeam,InviteToTeam

urlpatterns = [
    path('student/',GetAllStudents.as_view()),
    url(r'^student/(?P<pk>\d+)/$',GetStudent.as_view()),
    path('register/',RegisterStudent.as_view()),
    path('team/',CreateTeam.as_view()),
    path('invite/',InviteToTeam.as_view()),
]