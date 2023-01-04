from django.shortcuts import render
from rest_framework import generics
from api.serializers import UserSerializer
from api.models import User

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    