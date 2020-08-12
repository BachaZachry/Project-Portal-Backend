from rest_framework import serializers
from professors.models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id','first_name','last_name','email','speciality','grade']



class ProfessorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['email','password','first_name','last_name','grade','speciality']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = Professor.objects.create_user(**validated_data)
        return user