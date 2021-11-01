from .serializers import StudentSerializer, StudentRegisterSerializer, TeamSerializer, \
    InviteSerializer, InviteResponseSerializer, BulkCreateSerializer
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from django_filters import rest_framework as filters
from students.models import Student, Invite, Team
from users.permissions import CanCreateTeamStudent, IsLeader
from django.db.models import F
from django.core.mail import send_mail
from pyexcel_xls import get_data
from promo.models import Promo


# Get Student by id
class GetStudent(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Student.objects.all()

# Providing search functionality


class StudentFilter(filters.FilterSet):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'promo', 'note']

# Get All students


class GetAllStudents(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Student.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = StudentFilter


# Register as a student
class RegisterStudent(generics.GenericAPIView):
    serializer_class = StudentRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        return Response({
            "Professor": StudentRegisterSerializer(student, context=self.get_serializer_context()).data,
            "Id": student.id
        })

# Team Creation


class CreateTeam(generics.GenericAPIView):
    serializer_class = TeamSerializer
    permission_classes = [CanCreateTeamStudent]

    def post(self, request):
        '''
        This API view serves to create a team,it requires a student who has no team to be able
        to create a team.
        Upon team creation,it will get the leader's (student who created) note as it's average note
        '''

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Creating the team
        team = serializer.save()
        # Getting the student who created the team
        leader = serializer.context['request'].user.student
        # Assigning him the team he created
        leader.team = team
        leader.is_leader = True
        leader.save()
        # Initializing team note and number of members
        team.avg_note = leader.note
        team.number_of_members = 1
        # Saving the changes
        team.save()
        return Response({
            'Team Id': team.pk,
            'Team Name': team.name,
            'Team Leader Id': leader.id,
        })

# Invite


class InviteToTeam(generics.GenericAPIView):
    serializer_class = InviteSerializer
    permission_classes = [IsLeader]

    def post(self, request):
        '''
        This API view serves sending an invite
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Creating the invite
        invite = serializer.save()
        # Notifying the receiver
        # PS:Only use this when the production environment is secured
        # To test in dev environment
        # To send an email
        # Requires Conf on mail:Settings>Settings>Forwarding and POP/IMAP>Enable IMAP
        # Gmail Security>Allow Less Secure Apps>Activate
        # send_mail(
        #     'Invite Received',
        #     'You are invited to a team',
        #     'Admin Email',
        #     [receiver.email],
        #     fail_silently=False,
        # )

        return Response({
            'Invite': InviteSerializer(invite, context=self.get_serializer_context()).data,
            'Invite Id': invite.pk,
        })


class RespondToAnInvitation(generics.RetrieveUpdateAPIView):
    serializer_class = InviteSerializer
    permission_classes = [CanCreateTeamStudent]
    queryset = Invite.objects.all()

    def get_queryset(self):
        serializer = self.get_serializer()
        receiver = serializer.context['request'].user.student
        # Return only the invitations sent to that specific student
        return Invite.objects.filter(receiver=receiver)

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['status'] == 'A':
            receiver = serializer.context['request'].user.student
            sender_id = serializer.validated_data['sender']
            sender = Student.objects.get(pk=sender_id)
            # Adding to the team
            receiver.team = sender.team
            receiver.save()
            # Modifying Team attributes
            team = Team.objects.get(pk=receiver.team.pk)
            team.number_of_members += 1
            team.avg_note = (team.avg_note + receiver.note) / \
                team.number_of_members
            team.save()
        return self.update(request, *args, **kwargs)


class BulkCreateStudent(generics.GenericAPIView):
    serializer_class = BulkCreateSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['xls_file']
        data = get_data(file)
        promo = serializer.validated_data['promo']
        for i in range(1, len(data['Sheet1'])):
            first_name = data['Sheet1'][i][0].lower()
            last_name = data['Sheet1'][i][1].lower()
            note = data['Sheet1'][i][2]
            email = last_name[0] + '.' + first_name + '@esi-sba.dz'
            dummy_password = 'testinginprogress1'
            Student.objects.create_user(
                email=email, password=dummy_password, first_name=first_name, last_name=last_name, note=note, promo=promo)
        return Response({
            'Done': 'Yes'
        })
