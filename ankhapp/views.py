# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class WelcomeAPIView(APIView):
    """Test API Views"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'use HTTTP methods as function(get,post,patch,put,delete)'
            'is similar to django traditional view'
            'give u most control over application logic'
            'is mapped manually to urls'
        ]
        return Response({'message': 'Hello!','an_apiview': an_apiview})
