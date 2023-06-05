from rest_framework.serializers import ModelSerializer

from users.models import UserData


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = UserData
        fields = ('phone',)
