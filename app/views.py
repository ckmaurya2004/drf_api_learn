from django.shortcuts import render,HttpResponse
from django.http import JsonResponse,Http404
from . models import *
from .serializes import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from rest_framework import mixins,generics
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from rest_framework.authentication import BasicAuthentication,TokenAuthentication

from . permissions import * 
from rest_framework.authtoken.models import Token

# Create your views here.

class  CourseDetailView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListView (ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,WriteByAdminOnlyPermissions]
    queryset =Course.objects.all()
    serializer_class = CourseSerializer

class InsctructureListView (ModelViewSet):
    queryset =Insctructure.objects.all()
    serializer_class = InsctructureSerializer