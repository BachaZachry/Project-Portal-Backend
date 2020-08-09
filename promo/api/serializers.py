from rest_framework import serializers
from promo.models import Promo

#Serializer to create a promo

class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = ['id','cycle','year','specialityName','description','minTeamMembers','maxTeamMembers','maxTeamsInProject']