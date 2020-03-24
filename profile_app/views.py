
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import HelloSerializer

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
                 
