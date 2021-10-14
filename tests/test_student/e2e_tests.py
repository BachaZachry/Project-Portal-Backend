from factory.base import StubFactory
import pytest
from promo.models import Promo
from students.models import Student
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
