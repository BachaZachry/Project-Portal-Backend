from django.db import models
from users.models import User
from promo.models import Promo



class Team(models.Model):
    name = models.CharField(max_length=100,blank=True)
    avg_note = models.FloatField(null=True,blank=True)
    number_of_members = models.IntegerField(null=True,blank=True)


class Student(User):
    promo = models.ForeignKey(Promo,on_delete=models.CASCADE)

    note = models.IntegerField(null=True,blank=True)
    #In case of student object deletion,we can't delete the whole team object
    team = models.ForeignKey(Team,blank=True,null=True,on_delete=models.PROTECT)

    is_leader = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name
