import factory
from knox.models import AuthToken
import pytest
from rest_framework.test import APIClient
from professors.models import Professor
from students.models import Student

from tests.factories import ProfessorFactory, StudentFactory
from datetime import timedelta


class TestUserEndpoints:
    endpoint = '/users/login/'

    @pytest.mark.django_db
    def test_login_student(self, api_client):
        student = StudentFactory()
        expected_request_json = {
            'email': student.email,
            'password': 'pi3.1415'
        }

        response = api_client().post(
            '/users/login/', data=expected_request_json, format='json')
        assert response.status_code == 200
        assert response.json().get('Type') == 'student'

    @pytest.mark.django_db
    def test_login_professor(self, api_client):
        professor = ProfessorFactory()
        expected_request_json = {
            'email': professor.email,
            'password': 'pi3.1415'
        }
        response = api_client().post('/users/login/', data=expected_request_json,
                                     format="json")
        assert response.status_code == 200
        assert response.json().get('Type') == 'professor'

    @pytest.mark.django_db
    def test_modify_password(self, api_client):
        student = StudentFactory()
        token = AuthToken.objects.create(user=student)[1]

        current_pass = 'pi3.1415'
        new_pass = 'newpassword234'
        expected_request_json = {
            'current_password': current_pass,
            'new_password': new_pass
        }
        cli = api_client()
        cli.credentials(HTTP_AUTHORIZATION='Token %s' % token)
        response = cli.patch('/users/changepassword/',
                             data=expected_request_json)
        print(response)
        print(response.json())
        assert response.status_code == 200
