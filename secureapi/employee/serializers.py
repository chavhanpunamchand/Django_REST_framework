from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import Emp


class EmpSerialization(ModelSerializer):
    class Meta:
        model = Emp
        fields  = '__all__'

