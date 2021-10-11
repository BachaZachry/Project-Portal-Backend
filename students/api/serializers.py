from students.models import Student,Team,Invite
from rest_framework import serializers
from users.fields import CurrentStudent



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

class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['sender','receiver','status']
        extra_kwargs = {'sender':{'default':CurrentStudent()}}


class InviteResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['sender', 'receiver', 'status']

class BulkCreateSerializer(serializers.ModelSerializer):
    xls_file = serializers.FileField()
    class Meta:
        model = Student
        fields = ['promo','xls_file']