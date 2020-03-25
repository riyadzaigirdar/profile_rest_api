from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profile_app.permissions import UserProfilePermission,ProfileFeedPermission
from rest_framework.permissions import IsAuthenticated
from .serializers import HelloSerializer,UserProfileSerializer,ProfileFeedSerializer
from .models import UserProfile,profileFeed

class HelloApiView(APIView):

    serializer_class = HelloSerializer

    def get(self,request,format=None):
        an_apiview = [
            'uses HTTp method as function(get,post,patch,put,delete',
            'is similar to a traditional django view',
            'gives most control of your logic',
            'mapped manually to urls'
        ]
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message}) 
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'message': 'put'})

    def patch(self, request, pk=None):
        return Response({'message': 'patch'})

    def delete(self, request, pk=None):
        return Response({'message': 'delete'})


                
class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = [TokenAuthentication]   
    permission_classes = [UserProfilePermission]
    filter_backends = [SearchFilter]
    search_fields = ['id','email','name']
    
class UserLoginApi(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewset(viewsets.ModelViewSet):
    serializer_class = ProfileFeedSerializer
    queryset = profileFeed.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [ProfileFeedPermission,IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)

   

