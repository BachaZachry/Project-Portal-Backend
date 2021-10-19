import factory
import pytest
from professors.api.serializers import ProfessorRegisterSerializer
from professors.models import Professor
from tests.factories import ProfessorFactory


class TestProfessorSerializers:

    def test_serialize_model(self):
        professor = ProfessorFactory.build()
        serializer = ProfessorRegisterSerializer(professor)

        assert serializer.data

    @pytest.mark.django_db
    def test_serialized_data(self):
        professor = ProfessorFactory.build()
        expected_json = {
            'email': professor.email,
            'password': 'pi3.1415',
            'first_name': professor.first_name,
            'last_name': professor.last_name,
            'grade': professor.grade,
            'speciality': professor.speciality
        }
        serializer = ProfessorRegisterSerializer(data=expected_json)
        assert serializer.is_valid()
        assert serializer.errors == {}
