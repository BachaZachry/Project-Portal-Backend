import factory
from factory import fuzzy
from rest_framework.exceptions import ValidationError
from students.models import Student
from professors.models import Professor
from promo import models
import random
from django.contrib.auth.hashers import make_password

PROMO_CYCLE = [x[0] for x in models.Promo.choiceset]
PROMO_YEAR = [x[0] for x in models.Promo.choiceyear]
PROFESSOR_GRADES = [x[0] for x in Professor.grades]


class PromoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Promo

    while True:
        try:
            cycle = fuzzy.FuzzyChoice(PROMO_CYCLE)
            year = fuzzy.FuzzyChoice(PROMO_YEAR)
            if not (cycle == 'CPI' and year == "3rd"):
                break
        except ValidationError:
            pass
    specialityName = factory.Faker('name')
    minTeamMembers = factory.Faker('random_digit')
    maxTeamMembers = factory.Faker('random_digit')
    maxTeamsInProject = factory.Faker('random_digit')


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    email = factory.Faker('email')
    password = factory.LazyFunction(lambda: make_password('pi3.1415'))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    promo = factory.SubFactory(PromoFactory)
    note = factory.Faker('random_digit')


class ProfessorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Professor
    email = factory.Faker('email')
    password = factory.LazyFunction(lambda: make_password('pi3.1415'))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    grade = fuzzy.FuzzyChoice(PROFESSOR_GRADES)
    speciality = factory.Faker('name')
