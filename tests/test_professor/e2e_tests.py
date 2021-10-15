import pytest
from tests.factories import ProfessorFactory
from professors.models import Professor


class TestprofessorEndpoints:

    @pytest.mark.django_db
    def test_register(self, api_client):
        professor = ProfessorFactory.build()
        expected_json = {
            'email': professor.email,
            'password': 'pi3.1415',
            'first_name': professor.first_name,
            'last_name': professor.last_name,
            'grade': professor.grade,
            'speciality': professor.speciality
        }
        response = api_client().post('/professor/register/', data=expected_json)
        print(response.json())
        assert response.status_code == 200
        assert Professor.objects.all().count() == 1
