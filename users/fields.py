from rest_framework.fields import CurrentUserDefault


class CurrentStudent(CurrentUserDefault):
    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.student