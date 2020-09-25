from .serializers import ProfessorSerializer,ProfessorRegisterSerializer,PFESerializer \
    ,ProjectUpdateSerializer
from rest_framework import generics,permissions
from rest_framework.response import Response
from django_filters import rest_framework as filters
from professors.models import Professor,Project
from users.permissions import IsProfessor


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

#Register as a professor
class RegisterProfessor(generics.GenericAPIView):
    serializer_class = ProfessorRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        professor = serializer.save()
        return Response({
            "Professor":ProfessorRegisterSerializer(professor,context=self.get_serializer_context()).data,
            "Id":professor.id
        })

class ProjectSubmission(generics.CreateAPIView):
    serializer_class = PFESerializer
    permission_classes = [IsProfessor]


class ProjectUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectUpdateSerializer
    permission_classes = [IsProfessor]
    queryset = Project.objects.all()

    def get_queryset(self):
        '''A teacher can modify or delete only the projects he submitted'''
        serializer = self.get_serializer()
        professor = serializer.context['request'].user.professor
        return Project.objects.filter(professor=professor)

class ProjectEvaluation(generics.RetrieveUpdateAPIView):
    serializer_class = PFESerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Project.objects.all()



