import factory
from factory.base import StubFactory
from knox.models import AuthToken
import pytest
from promo.models import Promo
from students.models import Student, Team
from tests.factories import PromoFactory, StudentFactory


class TestStudentEndpoints:

    @pytest.mark.django_db
    def test_register(self, api_client):
        student = StudentFactory.build()
        promo = PromoFactory()
        expected_json = {
            'email': student.email,
            'password': 'pi3.1415',
            'first_name': student.first_name,
            'last_name': student.last_name,
            'promo': int(promo.id),
            'note': student.note
        }
        response = api_client().post('/student/register/', data=expected_json)
        print(response.json())
        assert response.status_code == 200
        assert Student.objects.all().count() == 1

    @pytest.mark.django_db
    def test_team_creation(self, api_client):
        leader = StudentFactory()
        team_name = factory.Faker('first_name')
        token = AuthToken.objects.create(user=leader)[1]
        cli = api_client()
        cli.credentials(HTTP_AUTHORIZATION='Token %s' % token)

        response = cli.post('/student/team/', data={'name': team_name})
        print(response.json())
        print(response)

        assert response.status_code == 200
        assert Team.objects.all().count() == 1
        assert response.json().get('Team Leader Id') == leader.id

    @pytest.mark.django_db
    def test_unauthorized_team_creation(self, api_client):
        leader = StudentFactory()
        team = Team.objects.create(name="test")
        leader.team = team
        leader.save()
        team_name = factory.Faker('first_name')
        token = AuthToken.objects.create(user=leader)[1]
        cli = api_client()
        cli.credentials(HTTP_AUTHORIZATION='Token %s' % token)

        response = cli.post('/student/team/', data={'name': team_name})
        print(response.json())
        print(response)

        assert response.status_code == 403
