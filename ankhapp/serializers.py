from rest_framework import serializers

from ankhapp import models


class WelcomeSerializer(serializers.Serializer):
    """serializer a name field for testing our APIView"""
    name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)


class LoginSerializer(serializers.Serializer):
    """serializer a name field for testing our APIView"""
    password = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)


class TaskSerializer(serializers.ModelSerializer):
    """task related operation"""

    class Meta:
        model = models.TaskDetails
        fields = ('task_id', 'task_name', 'task_description', 'created_by','assigned_to', 'task_duration', 'task_status')



class UserProfileSerializer(serializers.ModelSerializer):
    """serialize user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
