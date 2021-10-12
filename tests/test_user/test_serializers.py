import factory
import pytest
from students.models import Student

from tests.factories import StudentFactory
from users.api.serializers import LoginSerializer
import io
from rest_framework.parsers import JSONParser


class TestLoginSerializer:

    def test_serialize_model(self):
        student = StudentFactory.build()
        login_data = {
            'email': student.email,
            'password': 'pi3.1415'
        }
        serializer = LoginSerializer(login_data)

        assert serializer.data

    @pytest.mark.django_db
    def test_serialized_data(data):
        valid_serialized_data = StudentFactory()
        json = {
            'email': valid_serialized_data.email, 'password': 'pi3.1415'}
        serializer = LoginSerializer(
            data=json)
        assert serializer.is_valid()
        assert serializer.errors == {}
