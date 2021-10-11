import factory
import pytest
from professors.models import Professor
from students.models import Student

from tests.factories import ProfessorFactory, StudentFactory


class TestUserEndpoints:
    endpoint = '/users/login/'

    @pytest.mark.django_db
    def test_login_student(self, api_client):
        student = StudentFactory()
        print(Student.objects.all())
        expected_request_json = {
            'email': student.email,
            'password': 'pi3.1415'
        }

        response = api_client().post(self.endpoint, data=expected_request_json, format='json')
        print(response.json())
        assert response.status_code == 200
        assert response.json().get('Type') == 'student'

    @pytest.mark.django_db
    def test_login_professor(self, api_client):
        professor = ProfessorFactory()
        print(Professor.objects.all())
        expected_request_json = {
            'email': professor.email,
            'password': 'pi3.1415'
        }
        print(expected_request_json)
        response = api_client().post(self.endpoint, data=expected_request_json,
                                     format="json")
        print(response.json())
        assert response.status_code == 200
        assert response.json().get('Type') == 'professor'
