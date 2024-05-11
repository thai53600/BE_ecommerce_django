
from rest_framework import serializers
from user.models import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'first_name', 'last_name', '...']
class UserAccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('first_name', 'last_name', 'email', 'phone', 'address')

