from rest_framework import generics, permissions
from .serializers import LoginSerializer, PasswordChangeSerializer
from users.models import User
from rest_framework.response import Response
from django.db import connection
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
        :param kwargs: E-mail : String (runs validation if it's an e-mail form) + password
        :return: Token : String
                Id : String
                Role: admin, student or professor)
        in case of error it returns "Incorrect Credentials" .
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)[1]
        loggedin_user = User.objects.get(email=user.email)
        # Recognize whether it's a student,professor or admin that logged in
        if loggedin_user.is_staff is True:
            role = "admin"
        elif hasattr(loggedin_user, 'student') is True:
            role = "student"
        else:
            role = "professor"
        return Response({
            "token": token,
            "userId": object.id,
            "Type": role
        })


class ChangePassword(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.context['request'].user
        # Check if the current password is correct
        if user.check_password(serializer.validated_data['current_password']):
            user.set_password(serializer.validated_data['new_password'])
            user.save()
        else:
            raise ValueError('Incorrect Password')
        return Response("Password Changed Successfully!")
