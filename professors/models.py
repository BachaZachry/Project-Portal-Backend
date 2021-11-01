from django.db import models
from users.models import User
from promo.models import Promo


class Professor(User):
    grades = (
        ('MCA', 'MCA'),
        ('MCB', 'MCB'),
        ('MAA', 'MAA'),
        ('MAB', 'MAB'),
        ('Pr', 'Pr'),
    )
    speciality = models.CharField(max_length=50, blank=True, default='')
    grade = models.CharField(max_length=50, blank=True,
                             choices=grades, default=None)

    def __str__(self):
        if (self.grade == 'Pr'):
            return 'Professor ' + self.last_name + ' ' + self.first_name
        return 'Dr.' + self.last_name + ' ' + self.first_name


class Project(models.Model):
    title = models.CharField(max_length=256)
    domain = models.CharField(max_length=256)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    tools = models.TextField()
    required_documents = models.TextField()
    document = models.FileField()
    STATUS_CHOICES = (
        ("A", "Accepted"),
        ("P", "Pending"),
        ("R", "Rejected"),
    )
    status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, default='P')
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE)
