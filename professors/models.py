from django.db import models
from users.models import User

class Professor(User):
    grades = (
        ('MCA','MCA'),
        ('MCB','MCB'),
        ('MAA','MAA'),
        ('MAB','MAB'),
        ('Pr','Pr'),
    )
    speciality = models.CharField(max_length=50,blank=True,default='')
    grade = models.CharField(max_length=50,blank=False,choices=grades)

    def __str__(self):
        if (self.grade == 'Pr'):
            return 'Professor ' + self.lastName + ' ' + self.firstName
        else:
            return 'Dr.' + self.lastName + ' ' + self.firstName