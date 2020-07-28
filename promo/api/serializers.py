from rest_framework import serializers
from promo.models import Promo

#Serializer to create a promo

class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = ['cycle','year','specialityName','description','minTeamMembers','maxTeamMembers','maxTeamsInProject']
    def create(self, validated_data):
        promo = Promo.objects.create(**validated_data)
        return promo