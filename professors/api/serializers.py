from rest_framework import serializers
from professors.models import Professor,Project
from users.fields import CurrentProfessor


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

class PFESerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['promo','title','domain','tools','required_documents','document','professor','status']
        extra_kwargs = {'professor':{'default':CurrentProfessor()}}

class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['promo','title','domain','tools','required_documents','document']
