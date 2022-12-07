from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from .Serializers import DataSerializers
from .models import Data


class StudentCurd(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializers
    permission_classes = [permissions.AllowAny]
    

