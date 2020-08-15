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
    grade = models.CharField(max_length=50,blank=True,choices=grades,default=None)

    def __str__(self):
        if (self.grade == 'Pr'):
            return 'Professor ' + self.last_name + ' ' + self.first_name
        else:
            return 'Dr.' + self.last_name + ' ' + self.first_name