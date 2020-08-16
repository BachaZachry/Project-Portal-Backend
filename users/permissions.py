from rest_framework import permissions


#Student Permissions
class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.student and request.user.is_authenticated

#Professor Permissions
class IsProfessor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.professor and request.user.is_authenticated

#Student who are able to create teams
class CanCreateTeamStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.student and request.user.is_authenticated and request.user.student.is_leader == False \
            and request.user.student.team == None
