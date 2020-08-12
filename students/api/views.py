from .serializers import StudentSerializer,StudentRegisterSerializer
from rest_framework import generics,permissions
from rest_framework.response import Response
from django_filters import rest_framework as filters
from students.models import Student


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