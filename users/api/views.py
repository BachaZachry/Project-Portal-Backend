from rest_framework import generics,permissions
from .serializers import LoginSerializer
from users.models import User
from rest_framework.response import Response
from knox.auth import AuthToken

class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        '''
        POST
        A simple login api,it is used for both students and teachers
        :param request: POST
        :param args: None
        :param kwargs: username : String + E-mail : String (runs validation if it's an e-mail form) + password
        :return: Token : String
                Id : String
                Role: Integer (0: admin,1: student,2: professor)
        in case of error it returns "Incorrect Credentials" .
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)[1]
        object = User.objects.get(email=user.email)
        #Recognize whether it's a student,professor or admin that logged in
        if object.is_staff == True:
            role = 0
        elif hasattr(object,'student')==True:
            role = 1
        else:
            role = 2
        return Response({
            "token":token,
            "userId":object.id,
            "Type":role
        })
