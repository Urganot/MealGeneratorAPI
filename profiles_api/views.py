from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class HalloApiView(APIView):
    """Test API view."""

    def get(self, request, format=None):
        an_apiview = [
            "Uses HTTP methods as functions (get, post, patch, put, delete)",
            "Is similar to a traditional Django view",
            "Gives you the most control over your logic",
            "Is mapped manually to URLs",
        ]
        return Response({'message': "Hello", "an_apiview": an_apiview})
