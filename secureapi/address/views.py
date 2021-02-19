from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from  rest_framework_xml.renderers import XMLRenderer
from rest_framework.decorators import renderer_classes
from rest_framework.permissions import IsAuthenticated
class AddressOperations(ModelViewSet): #list
    permission_classes = (AllowAny,)
   #renderer_classes = (XMLRenderer,)
    queryset = Address.objects.all()
    serializer_class = AddressSerialization


class StudentOperations(ModelViewSet): #list
    permission_classes = (AllowAny,)
    queryset = Student.objects.all()
    serializer_class = StudentSerialization


class CoursesOperations(ModelViewSet): #list
    permission_classes = (AllowAny,)
    queryset = Courses.objects.all()
    serializer_class = CourseSerialization



