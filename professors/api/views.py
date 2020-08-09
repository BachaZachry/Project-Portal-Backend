from .serializers import ProfessorSerializer
from rest_framework import generics,permissions
from django_filters import rest_framework as filters
from professors.models import Professor


#Get Professor by id
class GetProfessor(generics.RetrieveAPIView):
    serializer_class = ProfessorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Professor.objects.all()

#Providing search functionality
class ProfessorFilter(filters.FilterSet):
    class Meta:
        model = Professor
        fields = ['first_name','last_name','email','speciality','grade']

#Get All professors
class GetAllProfessors(generics.ListAPIView):
    serializer_class = ProfessorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Professor.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProfessorFilter
