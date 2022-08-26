from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from .serializers import *


@api_view(['GET'])
def get_projects(request):
    try:
        projects = Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    except Exception as e:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': str(e.error)
        })
