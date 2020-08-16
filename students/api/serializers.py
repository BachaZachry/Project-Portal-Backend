from students.models import Student,Team
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','first_name','last_name','email','promo','note']



class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['email','password','first_name','last_name','promo','note']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = Student.objects.create_user(**validated_data)
        return user

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']