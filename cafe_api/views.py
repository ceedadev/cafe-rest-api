from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, put, delete)',
            'is similar to traditional Django view',
            'Gives you the most of application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
        