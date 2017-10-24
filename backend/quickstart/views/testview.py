from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

from django.contrib.auth.models import User
from quickstart.serializers import UserSerializer
from quickstart.httpmodel.test import SnippetSerializer

from quickstart.models import Blog
from django.utils import timezone

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(methods=['post'])
    def set_password(self, request, pk=None):
        return Response({'status': 'password set'})

    @list_route(methods=['post'])
    def recent_users(self, request):
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors)
        # blog = Blog(title='first Blog',author='Yang',publish_time=timezone.now(),content ='搜素我不是潘金莲')
        # blog.save()
        # return Response({'status': 'password set1'})