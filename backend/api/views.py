from django.shortcuts import render
from rest_framework import generics

class CustomDetail(generics.RetrieveDestroyAPIView):
    pass

class CustomList(generics.ListCreateAPIView):
    pass
    