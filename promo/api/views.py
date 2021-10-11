from .serializers import PromoSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from promo.models import Promo


# Get Promo by ID
class GetPromo(generics.RetrieveAPIView):
    serializer_class = PromoSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Promo.objects.all()


# Get All Promo's
class GetAllPromos(generics.ListAPIView):
    serializer_class = PromoSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Promo.objects.all()
