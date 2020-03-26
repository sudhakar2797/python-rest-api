from rest_framework import serializers


class WelcomeSerializer(serializers.Serializer):
    """serializer a name field for testing our APIView"""
    name=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=50)
    email=serializers.EmailField(max_length=50)