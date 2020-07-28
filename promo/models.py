from django.db import models
from rest_framework.exceptions import ValidationError

class Promo(models.Model):
    choiceset= (
        ('CPI','CPI'),
        ('SC','SC')
    )
    choiceyear = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd')
    )
    cycle = models.CharField(max_length=50,choices=choiceset)
    year = models.CharField(max_length=50,choices=choiceyear)
    specialityName= models.CharField(max_length=50,blank=True,default='Main Branch')
    description = models.TextField(blank=False)
    #Min team members in a team in a class
    minTeamMembers = models.IntegerField(default=4)
    #Max team members in a team in a class
    maxTeamMembers = models.IntegerField(default=6)
    #Max teams that can take a project in a class
    maxTeamsInProject = models.IntegerField(default=2)
    class Meta:
        unique_together = ('year','specialityName')
    def save(self, *args,**kwargs):
        if not (self.cycle=="CPI" and self.year=="3rd"):
            super(Promo, self).save(*args,**kwargs)
        else:
            raise ValidationError("3rd Year CPI doesn't exist.")
    def __str__(self):
        return self.year + 'year' + self.cycle + self.specialityName
