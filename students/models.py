from django.db import models
from users.models import User
from promo.models import Promo

class Student(User):
    promo = models.ForeignKey(Promo,on_delete=models.CASCADE)
    note = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.lastName + ' ' + self.firstName