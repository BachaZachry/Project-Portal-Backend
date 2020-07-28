from .serializers import PromoSerializer
from rest_framework import generics,permissions
from rest_framework.response import Response
from promo.models import Promo

class PromoAddApi(generics.GenericAPIView):
    serializer_class = PromoSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self,request):
        '''Config:
            Authorization : Token adminToken
           Body:
            {
            'cycle':'CPI' or 'SC',
            'year':'1st' or '2nd' or '3rd',
            'specialityName':'String',
            'description':'String',
            'minTeamMembers':int,
            'maxTeamMembers':int,
            'maxTeamsInProject':int,
            }
            Response:
            {Body,
            'Id':Promo Id(int)
            }

        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        promo = serializer.save()

        return Response({
            'Promo Added':PromoSerializer(promo,context=self.get_serializer_context()).data,
            'Id':promo.id,
        })

class PromoModifyApi(generics.RetrieveUpdateDestroyAPIView):
    '''Accepts:GET,PUT,DELETE Methods
    Config:
        Authorization:Token adminToken
    Params:
        Promo Id
    Body(Only PUT):
        'Field wanted to be changed':'appropriate value' (Check Add API)
    Response (Only PUT and GET):
        PromoSerializer
    '''
    serializer_class = PromoSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Promo.objects.all()