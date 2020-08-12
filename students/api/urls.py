from django.urls import path
from django.conf.urls import url
from .views import GetStudent,GetAllStudents,RegisterStudent

urlpatterns = [
    path('student/',GetAllStudents.as_view()),
    url(r'^student/(?P<pk>\d+)/$',GetStudent.as_view()),
    path('register/',RegisterStudent.as_view()),
]