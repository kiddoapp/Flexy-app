from rest_framework import serializers
from users.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'url', 'email', 'first_name', 'last_name', 'password', 'Age', 'phone_number', 'staysignin')
        extra_kwargs = {'password': {'write_only': True}}

    def create (self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.username = validated_data.get('email')
        user.Age = validated_data.get('Age')
        user.phone_number= validated_data.get('phone_number')
        user.staysignin = validated_data.get('staysignin')
        user.set_password(password)
        user.save()
        return user