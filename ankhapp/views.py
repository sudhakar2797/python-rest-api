# Create your views here.
from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from ankhapp import serializers, models, permissions
from ankhapp.models import UserProfile, UserProfileManager
from ankhapp.serializers import WelcomeSerializer, TaskSerializer
from django.contrib.auth.hashers import check_password


class WelcomeAPIView(APIView):
    """Test API Views"""
    serializer_class = WelcomeSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'use HTTTP methods as function(get,post,patch,put,delete)'
            'is similar to django traditional view'
            'give u most control over application logic'
            'is mapped manually to urls'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Returns data with post call"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            name = serializer.validated_data.get('name')
            password = serializer.validated_data.get('password')
            message = f'Welcome {name},{email},{password}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Return Put method response replace"""
        return Response({'message': 'PUT response'})

    def patch(self, request, pk=None):
        """Return Patch method response update"""
        return Response({'message': 'Patch response'})

    def delete(self, request, pk=None):
        """Return Delete method response delete"""
        return Response({'message': 'Delete response'})


class WelcomeViewSet(viewsets.ViewSet):
    """API viewset"""
    serializer_class = serializers.WelcomeSerializer

    def list(self, request):
        """return a hello message"""
        a_viewset = ['user action[update,partial update,delete,retrieve]',
                     'automatically map to route urls',
                     'provide more functionality with less code']
        return Response({'message': a_viewset})

    def create(self, request):
        """create new user message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'welcome {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """update row with primary key"""
        return Response({'message': 'GET'})

    def update(self, request, pk=None):
        """update row with primary key"""
        return Response({'message': 'PUT'})

    def partial_update(self, request, pk=None):
        """update row with primary key"""
        return Response({'message': 'PATCH'})

    def destroy(self, request, pk=None):
        """update row with primary key"""
        return Response({'message': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class CheckValidUser(APIView):
    """Check user credentials"""
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        """Returns data with post call"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            data = models.UserProfile.objects.get(email=email)
            if check_password(password, data.password):
                if email == 'sudhakar.it.12345@gmail.com':
                    role = 'admin'
                else:
                    role = 'user'
                return Response({'login': 'success', 'role': role,'id':data.id})
            else:
                return Response({"msg": "unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailsViewSet(viewsets.ModelViewSet):
    """return user task details"""
    serializer_class = TaskSerializer
    queryset = models.TaskDetails.objects.all().order_by('task_id').order_by('task_status')
