# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ankhapp.serializers import WelcomeSerializer


class WelcomeAPIView(APIView):
    """Test API Views"""
    serializer_class=WelcomeSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'use HTTTP methods as function(get,post,patch,put,delete)'
            'is similar to django traditional view'
            'give u most control over application logic'
            'is mapped manually to urls'
        ]
        return Response({'message': 'Hello!','an_apiview': an_apiview})

    def post(self,request):
        """Returns data with post call"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Welcome {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)