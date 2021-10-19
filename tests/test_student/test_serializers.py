import factory
import pytest
from students.api.serializers import StudentRegisterSerializer
from students.models import Student
from tests.factories import StudentFactory, PromoFactory


class TestStudentSerializers:

    def test_serialize_model(self):
        student = StudentFactory.build()
        serializer = StudentRegisterSerializer(student)

        assert serializer.data

    @pytest.mark.django_db
    def test_serialized_data(self):
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
        serializer = StudentRegisterSerializer(data=expected_json)
        assert serializer.is_valid()
        assert serializer.errors == {}
