from django.db import models
from users.models import User
from promo.models import Promo
from django.core.exceptions import ValidationError



class Team(models.Model):
    name = models.CharField(max_length=100,blank=True)
    avg_note = models.FloatField(null=True,blank=True)
    number_of_members = models.IntegerField(null=True,blank=True)


class Student(User):
    promo = models.ForeignKey(Promo,on_delete=models.CASCADE)

    note = models.IntegerField(null=True,blank=True)
    #In case of team deletion,we can't delete the student
    team = models.ForeignKey(Team,blank=True,null=True,on_delete=models.SET_NULL)

    is_leader = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

class Invite(models.Model):
    STATUS_CHOICES = (
        ('P','Pending'),
        ('A','Accepted'),
        ('R','Rejected')
    )
    sender = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='Sender')
    receiver = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='Receiver')
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='P')

    def save(self,*args,**kwargs):
        if (self.sender==self.receiver):
            raise ValidationError("Sender can't invite himself")
        else:
            super(Invite,self).save(*args,**kwargs)