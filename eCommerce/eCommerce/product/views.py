from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from .import Serializers

class CategoryViewSet(viewsets.ViewSet):
    
    queryset=models.Category.objects.all()
    
    def list(self, request):
        
        serializer = Serializers.CategorySerializer(self.queryset,many=True)
        
        return Response(serializer.data)