from .serializers import StudentSerializer,StudentRegisterSerializer,TeamSerializer
from rest_framework import generics,permissions
from rest_framework.response import Response
from django_filters import rest_framework as filters
from students.models import Student
from users.permissions import CanCreateTeamStudent


#Get Student by id
class GetStudent(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Student.objects.all()

#Providing search functionality
class StudentFilter(filters.FilterSet):
    class Meta:
        model = Student
        fields = ['first_name','last_name','email','promo','note']

#Get All students
class GetAllStudents(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Student.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = StudentFilter

#Register as a student
class RegisterStudent(generics.GenericAPIView):
    serializer_class = StudentRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        return Response({
            "Professor":StudentRegisterSerializer(student,context=self.get_serializer_context()).data,
            "Id":student.id
        })

#Team Creation
class CreateTeam(generics.GenericAPIView):
    serializer_class = TeamSerializer
    permission_classes = [CanCreateTeamStudent]

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #Creating the team
        team = serializer.save()
        #Getting the student who created the team
        leader = serializer.context['request'].user.student
        #Assigning him the team he created
        leader.team = team
        leader.is_leader = True
        leader.save()
        #Initializing team note and number of members
        team.avg_note = leader.note
        team.number_of_members = 1
        #Saving the changes
        team.save()
        return Response({
            'Team Id':team.pk,
            'Team Name':team.name,
            'Team Leader Id':leader.id
        })
