from rest_framework import serializers
from professors.models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id','first_name','last_name','email','speciality','grade']