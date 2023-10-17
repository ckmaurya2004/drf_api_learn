from rest_framework import serializers
from django.contrib.auth .models import User
from . models import *

class  EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name =serializers.CharField(max_length=50) 
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)


class  CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class  InsctructureSerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(many =True,read_only = True,view_name="course_deatal")
    class Meta:
        model = Insctructure
        fields = '__all__'
