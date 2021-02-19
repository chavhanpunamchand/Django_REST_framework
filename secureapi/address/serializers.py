from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import *


class AddressSerialization(ModelSerializer):
    class Meta:
        model = Address
        fields  = '__all__'



class CourseSerialization(HyperlinkedModelSerializer):
   # students = StudentSerialization(many=False)
    class Meta:
        model = Courses
        fields  = '__all__'#('coursename','coursefees')

class StudentSerialization(HyperlinkedModelSerializer):
    courses = CourseSerialization(many=True)
    class Meta:
        model = Student
        fields  = '__all__'



#fields -- all --> all fields from model
# fields -- (1,2,3) --> only specified fields
#exclude --> except these
